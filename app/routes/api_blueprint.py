from flask import Blueprint

from app.routes.account_blueprint import bp_account
from app.routes.transaction_blueprint import bp_transaction

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_account)
bp_api.register_blueprint(bp_transaction)
