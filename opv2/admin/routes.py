import random
from flask import (Flask, Blueprint, render_template, url_for, Response, send_file, request, session, jsonify,
                   make_response, redirect, flash)
from flask_cachecontrol import dont_cache, cache
from datetime import datetime, timedelta
from opv2 import mycursor, mydb, create_firma_token
from opv2.mysql_handler import sql_get, sql_insert, sql_update

admin = Blueprint("admin", __name__, url_prefix="/admin", template_folder='templates')


@admin.route("/home")
@dont_cache()
def home_page():
    if session.get("opravneni") == "Admin":
        return render_template("admin/home.html")
    else:
        return redirect(url_for("login_api.login_page"))


@admin.route("/profile", methods=["POST", "GET"])
@dont_cache()
def profile_page():
    user_id = session.get("user_id")
    if request.method == "POST":
        pass
    if session.get("user_id"):
        return render_template("admin/profile.html")
    else:
        return redirect(url_for("login_api.login_page"))


@admin.route("/seznam_firem/<stav>", methods=["POST", "GET"])
@dont_cache()
def list_of_companies(stav):
    if session.get("opravneni") == "Admin":
        if request.method == "POST":
            if request.form.get("firma"):
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
                    return redirect(request.url)
            if request.form.get("token"):
                token = create_firma_token(int(request.form["expire"]))
                flash(token, "create_token")
                return redirect(request.url)

        firmy = sql_get.get_company_list_by_category(stav)
        return render_template("admin/list_of_companies.html", firmy=firmy, stav=stav)
    else:
        return redirect(url_for("user.home_page"))


@admin.route("/seznam_ucitelu")
@dont_cache()
def list_of_teachers():
    if session.get("opravneni") == "Admin":
        teachers = sql_get.get_teacher_list()
        return render_template("admin/list_of_teachers.html", teachers=teachers)
    else:
        return redirect(url_for("user.home_page"))


@admin.route("/seznam_zaku")
@dont_cache()
def list_of_students():
    if session.get("opravneni") == "Admin":
        students = sql_get.get_students_list()
        return render_template("admin/list_of_students.html", students=students)
    else:
        return redirect(url_for("user.home_page"))


@admin.route("/praxe", methods=["GET", "POST"])
@dont_cache()
def list_of_praxe():
    if session.get("opravneni") == "Admin":
        if request.method == "POST":
            sql_insert.insert_praxe(request.form["floatingTrida"],
                                    datetime.now().year - 1 if datetime.now().month < 9 else datetime.now().year,
                                    request.form["floatingZacatek"], request.form["floatingKonec"])
            return redirect(url_for("admin.list_of_praxe"))
        mycursor.execute(f"select distinct nazev from uzivatel join trida on Id_trida = aktualni_trida order by nazev")
        tridy = mycursor.fetchall()
        praxe = sql_get.get_praxe_list()

        return render_template("admin/list_of_praxe.html", tridy=tridy, praxe=praxe)
    else:
        return redirect(url_for("user.home_page"))


@admin.route("/praxe/<trida>/<rok>", methods=["GET", "POST"])
@dont_cache()
def praxe(trida, rok):
    if session.get("opravneni") == "Admin":
        if request.method == "POST":
            zaci = [k for k, v in request.form.items() if v == "on"]
            sql_insert.insert_ucitel_to_praxe(zaci, request.form.get("ucitel"))
        students = sql_get.get_zaci_in_praxe(trida, rok)
        ucitele = sql_get.get_ucitele_in_praxe(trida, rok)
        vyber_ucitele = sql_get.get_teacher_list()
        dny_praxe = sql_get.get_dny_praxe(trida, rok)

        return render_template("admin/praxe.html", students=students, ucitele=ucitele, vyber_ucitele=vyber_ucitele,
                               dny_praxe=dny_praxe)
    else:
        return redirect(url_for("user.home_page"))


@admin.route("/uzivatel/<user>")
@dont_cache()
def user_profile(user):
    if session.get("opravneni") == "Admin":
        user = sql_get.get_user_by_email(user)
        return render_template("admin/user_profile.html", user=user)
    else:
        return redirect(url_for("user.home_page"))


@admin.route("/firma/<company>", methods=["GET", "POST"])
@dont_cache()
def company_profile(company):
    if session.get("opravneni") == "Admin":
        if request.method == "POST":
            sql_update.update_company([
                request.form["stav"],  # 0
                request.form["nazev"],  # 1
                request.form["ICO"],  # 2
                request.form["mesto_vykon"],  # 3
                request.form["ulice_vykon"],  # 4
                request.form["psc_vykon"],  # 5
                request.form["mesto_sidlo"],  # 6
                request.form["ulice_sidlo"],  # 7
                request.form["psc_sidlo"],  # 8
                request.form.get("IT", False),  # 9
                request.form.get("ELE", False),  # 10
                request.form.get("PROJEKT", False),  # 11
                request.form.get("VOS", False),  # 12
                request.form["zastupce"],  # 13
                request.form["web"],  # 14
                request.form["cinnost"],  # 15
                request.form["pomucky"],  # 16
                request.form["poznamka"],  # 17
                company  # 18
            ])
            return redirect(request.url)

        firma = sql_get.get_company_by_id(company)
        if firma:
            return render_template("admin/company_profile.html", firma=firma)
    else:
        return redirect(url_for("user.home_page"))


@admin.route("/loader")
def loader():
    return render_template("admin/loader.html")


@admin.route("/fetch_calendar")
def fetch_calendar():
    if session.get("opravneni") == "Admin":
        colors = {"A": "#ffc107",
                  "B": "#0d6efd",
                  "C": "#dc3545",
                  "D": "#fd7e14",
                  "V": "#20c997"}
        events = [{
            "title": praxe[0],
            "start": praxe[1].isoformat(),
            "end": (praxe[2] + timedelta(days=1)).isoformat(),
            "color": colors[praxe[0][:1]]
        } for praxe in sql_get.get_praxe_list() if praxe is not None]
        return jsonify(events)
    return redirect(url_for("login_api.login_page"))
