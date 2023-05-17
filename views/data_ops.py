from flask import request, render_template, redirect, url_for, Blueprint
from controllers import get_current_username, send_raw_data, get_raw_data

bp = Blueprint("data_ops", __name__, template_folder="../templates")

@bp.route("/raw_data")
def raw_data():
    username, login_auth = get_current_username()
    raw_data = get_raw_data()
    return render_template("raw_data.html", username=username, login_auth=login_auth, raw_data=raw_data)

@bp.route("/send_cmd", methods=["GET", "POST"])
def send_cmd():
    username, login_auth = get_current_username()
    if request.method == "POST":
        if request.form:
            name = request.form.get("name")
            email = request.form.get("email")
            category = request.form.get("category")
            test = request.form.get("priority")
            message = request.form.get("message")
            send_raw_data(name, email, category, test, message)
            return redirect(url_for("data_ops.send_cmd"))
    return render_template("send_cmd.html", username=username, login_auth=login_auth)

@bp.route("/charts")
def charts():
    username, login_auth = get_current_username()

    data = [
        ("15:19", 45.26),
        ("15:20", 45.0),
        ("15:21", 40.32),
        ("15:22", 55.43),
        ("15:23", 75.88),
        ("15:26", 34.6)
    ]

    data2 = [
        ("15:19", 123),
        ("15:20", 45),
        ("15:21", 55),
        ("15:22", 34),
        ("15:23", 88),
        ("15:26", 95),
        ("15:26", 95),
        ("15:26", 95)

    ]

    data3 = [
        ("15:19", 12.4),
        ("15:20", 12.3),
        ("15:21", 12.0),
        ("15:22", 12.2),
        ("15:23", 11.9),
        ("15:26", 11.4)
    ]

    if (len(data2) > 10):
        data2.pop(0)
        data2.pop(0)
        data2.pop(0)
        data2.pop(0)

    context_data = {
        "labels1": [row[0] for row in data],
        "values1": [row[1] for row in data],
        "labels2": [row[0] for row in data2],
        "values2": [row[1] for row in data2],
        "labels3": [row[0] for row in data3],
        "values3": [row[1] for row in data3]
    }


    return render_template("charts.html", username=username, login_auth=login_auth, **context_data)