from flask import render_template, Blueprint
from controllers import get_current_username

bp = Blueprint("home", __name__, template_folder="../templates")

@bp.route("/")
def index():
    username, login_auth = get_current_username()
    return render_template("index.html", username=username, login_auth=login_auth)


