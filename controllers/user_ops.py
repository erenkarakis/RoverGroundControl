from flask import session

def user_login(username, password):
    if username == "admin" and password == "admin":
        session["username"] = username
        return True
    else:
        return False

def user_logout():
    if "username" in session:
        del session["username"]
        return True
    else:
        return False

def get_current_username():
    username = ""
    login_auth = False
    if "username" in session:
        username = session["username"]
        login_auth = True
    return username, login_auth