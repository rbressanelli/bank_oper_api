from flask import Blueprint

from app.controllers.accounts_controller import (block_account, create_account,
                                                 delete_account, get_accounts)

bp_account = Blueprint("account", __name__, url_prefix="/accounts")

bp_account.get("")(get_accounts)

bp_account.post("/create/<string:user_id>")(create_account)

bp_account.delete("/<string:account_id>")(delete_account)

bp_account.put("/<string:account_id>/block")(block_account)
