from flask import Blueprint

from app.controllers.accounts_controller import create_account, delete_account, get_accounts

bp_account = Blueprint("account", __name__, url_prefix="/accounts")

bp_account.get("")(get_accounts)

bp_account.post("/create")(create_account)

bp_account.delete("/<string:account_id>")(delete_account)
