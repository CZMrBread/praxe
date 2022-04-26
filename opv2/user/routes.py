from flask import (Blueprint, render_template, url_for, Response, send_file, request, session, jsonify, make_response,
                   redirect, flash)
from flask_cachecontrol import dont_cache, cache
from datetime import timedelta
from opv2 import mycursor, mydb, verify_firma_token
from opv2.mysql_handler import sql_insert, sql_update, sql_get

user = Blueprint("user", __name__, template_folder='templates', static_folder="static")


@user.route("/home")
@dont_cache()
def home_page():
    if session.get("user_id"):
        if session.get("opravneni") == "Admin":
            return redirect(url_for("admin.home_page"))
        jmeno = sql_get.get_user_by_id(session.get("user_id"))
        jmeno = jmeno[1] + " " + jmeno[2]
        return render_template("user/home.html", jmeno=jmeno)
    else:
        return redirect(url_for("login_api.login_page"))


@user.route("/profile", methods=["POST", "GET"])
@dont_cache()
def profile_page():
    user_id = session.get("user_id")
    user = sql_get.get_user_by_id(user_id)
    if request.method == "POST":
        return redirect(url_for("user.profile_page"))

    if session.get("user_id"):
        return render_template("user/profile.html", user=user)
    else:
        return redirect(url_for("login_api.login_page"))


@user.route("/denik", methods=["GET", "POST"])
@dont_cache()
def diary_page():
    if session.get("user_id"):
        mycursor.execute(
            f"select nazev from uzivatel join trida on Id_trida = aktualni_trida where Id_uzivatel = '{session['user_id']}'")
        trida = mycursor.fetchone()[0]
        return render_template("user/diary.html", trida=trida)
    else:
        return redirect(url_for("login_api.login_page"))


@user.route("/denik/<den>", methods=["GET", "POST"])
@dont_cache()
def day_page(den):
    if session.get("user_id"):
        return render_template("user/day_page.html", den=den)
    else:
        return redirect(url_for("login_api.login_page"))


@user.route("/seznam_firem/<stav>")
@dont_cache()
def list_of_companies(stav):
    if session.get("user_id"):
        if stav in ["schvalena", "akceptovatelna"]:
            firmy = sql_get.get_company_list_by_category(stav)
            return render_template("user/list_of_companies.html", firmy=firmy, stav=stav)
        else:
            stav = "schvalena"
            firmy = sql_get.get_company_list_by_category(stav)
            return render_template("user/list_of_companies.html", firmy=firmy, stav=stav)
    else:
        return redirect(url_for("login_api.login"))


@user.route("/firma/<company>", methods=["GET", "POST"])
@dont_cache()
def company_profile(company):
    if session.get("user_id"):
        firma = sql_get.get_company_by_id(company)
        if firma:
            instruktori = sql_get.get_instruktori_by_firma(firma[0])
            return render_template("user/company_profile.html", firma=firma, instruktori=instruktori)
        else:
            return redirect(url_for("login_api.login"))
    else:
        return redirect(url_for("login_api.login"))


@user.route("/pridat_firmu/<token>", methods=["GET", "POST"])
def add_company(token):
    if request.method == "POST":
        success = sql_insert.insert_company([
            request.form["nazev"],  # 0
            request.form["ICO"],  # 1
            request.form["mesto_vykon"],  # 2
            request.form["ulice_vykon"],  # 3
            request.form["psc_vykon"],  # 4
            request.form["mesto_sidlo"],  # 5
            request.form["ulice_sidlo"],  # 6
            request.form["psc_sidlo"],  # 7
            request.form.get("IT", False),  # 8
            request.form.get("ELE", False),  # 9
            request.form.get("PROJEKT", False),  # 10
            request.form.get("VOS", False),  # 11
            request.form["zastupce"],  # 12
            request.form["web"],  # 13
            request.form["cinnost"],  # 14
            request.form["pomucky"],  # 15
            request.form["poznamka"]  # 16
        ])
        if not success:
            flash("Firma s tímto IČO je již přidaná", "ICO")
            return redirect(url_for("login_api.login"))
        mycursor.execute(r"delete from tokens where token=%s", (token,))
        mydb.commit()
        return redirect(url_for("user.home_page"))
    token = verify_firma_token(token)
    if token:
        return render_template("user/add_company.html")
    else:
        flash("Token vypršel nebo je neplatný", "token")
        return redirect(url_for("login_api.login"))


@user.route("/about")
def about_page():
    return render_template("user/about.html")


@user.route("/fetch_calendar")
def fetch_calendar():
    if session.get("user_id"):
        praxe = sql_get.get_praxe_by_zak(session.get("user_id"))
        if praxe is not None:
            events = [{
                "title": praxe[5],
                "start": praxe[6].isoformat(),
                "end": (praxe[7] + timedelta(days=1)).isoformat()
            }]
        else:
            events = ""
        return jsonify(events)
    return redirect(url_for("login_api.login_page"))
