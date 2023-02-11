from flask import request, redirect, render_template, abort, url_for, Blueprint
from controllers import user_login, user_logout ,get_current_username

bp = Blueprint("user_ops", __name__, template_folder="../templates")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if  request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if user_login(username, password):
                    return redirect(url_for('home.index'))
                else:
                    return redirect(url_for('user_ops.login'))
            pass
        abort(400)
    username, login_auth = get_current_username()
    return render_template("login.html", username=username, login_auth=login_auth)

@bp.route("/logout")
def logout():
    if user_logout():
        return redirect(url_for('home.index'))