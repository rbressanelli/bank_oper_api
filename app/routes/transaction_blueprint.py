from flask import Blueprint

from app.controllers.transactions_controller import (create_deposit,
                                                     create_withdraw,
                                                     get_balance, get_extract)

bp_transaction = Blueprint("transaction", __name__, url_prefix="/transactions")

bp_transaction.post("/create/<string:account_id>/deposit")(create_deposit)

bp_transaction.get("/<string:account_id>/balance")(get_balance)

bp_transaction.post("/create/<string:account_id>/withdraw")(create_withdraw)

bp_transaction.get("/<string:account_id>/extract")(get_extract)
