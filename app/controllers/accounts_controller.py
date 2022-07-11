from http import HTTPStatus
from sqlalchemy.orm.session import Session
import uuid

from flask import current_app, jsonify, request
from app.models.accounts_model import AccountModel
from app.services.auxiliar_functions import date_maker


def create_account():

    new_account = request.get_json()
    session: Session = current_app.db.session
    print(request.get_json())
    try:
        new_account["id"] = uuid.uuid4()
        new_account["created_at"] = date_maker()
        new_account["user_id"] = "12"

        new_account_data = AccountModel(**new_account)
        print(new_account_data)
        session.add(new_account_data)
        session.commit()
    except Exception as e:
        print(e)
        return jsonify()

    new_account_registered = AccountModel.query.filter_by(
        user_id=new_account["user_id"]
    ).first()

    return jsonify(new_account_registered), HTTPStatus.CREATED


def get_accounts():

    accounts = AccountModel.query.order_by(AccountModel.id)
    output = [account for account in accounts]

    if not output:
        return {"message": "No data"}, HTTPStatus.NOT_FOUND

    return jsonify(output[::-1]), HTTPStatus.OK


def delete_account(account_id: str):
    session: Session = current_app.db.session
    
    account_to_be_deleted = AccountModel.query.filter_by(account_id=account_id).first()
    
    if not account_to_be_deleted:
        return {
            "message":"No data"
        }, HTTPStatus.NOT_FOUND
        
    
    session.delete(account_to_be_deleted)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
