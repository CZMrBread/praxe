from flask import Blueprint, render_template, url_for, Response, send_file, request, session, jsonify, make_response, \
    redirect, flash
from opv2 import mysql_handler as handler
from opv2 import ldap_handler
from opv2 import ldap_server
from ldap3 import Connection, SAFE_SYNC
from opv2.mysql_handler import sql_insert, sql_update, sql_get

login_api = Blueprint("login_api", __name__, template_folder='templates')


@login_api.route("/")
def login_page():
    # ldap_handler.insert_students()
    if session.get("user_id"):
        return redirect(url_for("user.home_page"))
    else:
        return render_template("login_api/index.html")


@login_api.route("/logout")
def logout():
    print("logging out")
    session.clear()
    print(session)
    return redirect(url_for("login_api.login_page"))


@login_api.route("/login", methods=["POST", "GET"])
def login():
    obj = {}
    # print("request for login_api")
    if request.method == "POST":
        email = request.form["floatingEmail"]
        check = sql_get.get_user_by_email(email)
        if check is None:
            flash("is-invalid", "email")
            return redirect(url_for("login_api.login_page"))
        password = request.form["floatingPassword"]
        # print(email, password)

        try:
            # Connection(ldap_server, email, password, client_strategy=SAFE_SYNC, auto_bind=True)
            verif = True
        except:
            verif = False

        if verif:
            user = sql_get.get_user_by_email(email)
            session["user_id"] = user[0]
            session["opravneni"] = user[6]
            print(session)
            return redirect(url_for("user.home_page"))
        else:
            flash("is-invalid", "password")
            flash(email, "email_reuse")
            return redirect(url_for("login_api.login_page"))
    else:
        print(request.method)
        return redirect(url_for("login_api.login_page"))
