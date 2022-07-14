from datetime import date
from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import Forbidden, NotFound, Unauthorized

from app.exc import WithdrawLimitError
from app.models.accounts_model import AccountModel
from app.models.transaction_model import TransactionModel
from app.models.user_model import UserModel
from app.services.auxiliar_functions import date_maker, only_date


def create_deposit(account_id):

    new_deposit = request.get_json()
    session: Session = current_app.db.session

    try:
        account = AccountModel.query.filter_by(account_id=account_id).first()

        if not account:
            raise NotFound
        elif not account.is_active:
            raise Forbidden

        new_deposit["transaction_date"] = date_maker()
        new_deposit["account_id"] = account_id

        new_deposit_data = TransactionModel(**new_deposit)
        session.add(new_deposit_data)

        account.balance += new_deposit_data.value

        session.commit()

        return jsonify(new_deposit_data), HTTPStatus.CREATED

    except NotFound:
        return {"message": "Account not found"}, HTTPStatus.NOT_FOUND

    except Forbidden:
        return {"message": "Action not permitted"}, HTTPStatus.FORBIDDEN

    except:
        return {"message": "Internal error"}, HTTPStatus.INTERNAL_SERVER_ERROR


def get_balance(account_id):

    try:
        account = AccountModel.query.filter_by(account_id=account_id).first()

        if not account:
            raise NotFound

        user = UserModel.query.filter_by(user_id=account.user_id).first()

        return jsonify({"saldo": f"{account.balance:.2f}", "user": user}), HTTPStatus.OK

    except NotFound:
        return jsonify({"error": "Account not found"}), HTTPStatus.NOT_FOUND


def create_withdraw(account_id):

    new_withdraw = request.get_json()
    session: Session = current_app.db.session

    try:
        account = AccountModel.query.filter_by(account_id=account_id).first()
        transactions = TransactionModel.query.filter_by(account_id=account_id).all()

        if account and abs(new_withdraw["value"]) > account.daily_withdraw_limit:
            raise WithdrawLimitError("Value above daily withdraw limit.")

        new_withdraw["value"] *= -1

        total_value = sum(
            [
                transaction.value
                for transaction in transactions
                if transaction.value < 0
                and only_date(transaction.transaction_date) == date.today()
            ]
        )

        if (
            abs(new_withdraw["value"]) + abs(total_value)
        ) > account.daily_withdraw_limit:
            limit = account.daily_withdraw_limit - abs(total_value)
            raise WithdrawLimitError(
                f"Daily withdraw limit already reached. You can withdraw {limit:.2f}"
            )

        if not account:
            raise NotFound
        elif not account.is_active:
            raise Forbidden
        elif account.balance < abs(new_withdraw["value"]):
            raise Unauthorized

        new_withdraw["transaction_date"] = date_maker()
        new_withdraw["account_id"] = account_id

        new_withdraw_data = TransactionModel(**new_withdraw)
        session.add(new_withdraw_data)

        account.balance += new_withdraw_data.value

        session.commit()

        return jsonify(new_withdraw_data), HTTPStatus.CREATED

    except NotFound:
        return {"message": "Account not found"}, HTTPStatus.NOT_FOUND

    except Forbidden:
        return {"message": "Action not permitted"}, HTTPStatus.FORBIDDEN

    except Unauthorized:
        return {"message": "Insufficient funds"}, HTTPStatus.UNAUTHORIZED

    except WithdrawLimitError as err:
        return {"message": str(err)}, HTTPStatus.UNAUTHORIZED


def get_extract(account_id):

    try:
        account = AccountModel.query.filter_by(account_id=account_id).first()

        if not account:
            raise NotFound
        elif not account.is_active:
            raise Forbidden

        user = UserModel.query.filter_by(user_id=account.user_id).first()
        transactions = TransactionModel.query.filter_by(account_id=account_id).all()

        return jsonify(
            {
                "user": user,
                "account": account,
                "extract": [
                    {
                        "transaction_id": transaction.transaction_id,
                        "account_id": transaction.account_id,
                        "value": f"{transaction.value:.2f}",
                        "date": transaction.transaction_date,
                    }
                    for transaction in transactions
                ],
            }
        )

    except NotFound:
        return {"message": "Account not found"}, HTTPStatus.NOT_FOUND

    except Forbidden:
        return {"message": "Action not permitted"}, HTTPStatus.FORBIDDEN

    except:        
        return {"message": "Internal error"}, HTTPStatus.INTERNAL_SERVER_ERROR
