from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound

from app.models.accounts_model import AccountModel
from app.services.auxiliar_functions import date_maker


def create_account(user_id: str):

    new_account = request.get_json()
    session: Session = current_app.db.session

    try:
        new_account["created_at"] = date_maker()
        new_account["user_id"] = user_id

        new_account_data = AccountModel(**new_account)
        session.add(new_account_data)
        session.commit()

    except IntegrityError as e:        
        return jsonify(str(e.orig))        

    new_account_registered = AccountModel.query.filter_by(
        user_id=new_account["user_id"]
    ).first()

    return jsonify(new_account_registered), HTTPStatus.CREATED


def get_accounts():

    accounts = AccountModel.query.order_by(AccountModel.account_id)
    output = [account for account in accounts]

    if not output:
        return {"message": "No data"}, HTTPStatus.NOT_FOUND

    return jsonify(output[::-1]), HTTPStatus.OK


def delete_account(account_id: str):
    session: Session = current_app.db.session

    account_to_be_deleted = AccountModel.query.filter_by(account_id=account_id).first()

    if not account_to_be_deleted:
        return {"message": "No data"}, HTTPStatus.NOT_FOUND

    session.delete(account_to_be_deleted)
    session.commit()

    return "", HTTPStatus.NO_CONTENT


def block_account(account_id):
    session: Session = current_app.db.session

    try:
        account_to_be_blocked = AccountModel.query.filter_by(
            account_id=account_id
        ).first()

        if not account_to_be_blocked:
            raise NotFound

        account_to_be_blocked.is_active = False

        session.add(account_to_be_blocked)
        session.commit()

        return "", HTTPStatus.NO_CONTENT

    except NotFound:
        return jsonify({"error": "Account not found"}), HTTPStatus.NOT_FOUND
