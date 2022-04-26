from flask import Flask
from flask_cachecontrol import FlaskCacheControl
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from opv2.asset import Asset
import jwt
import mysql.connector
import datetime
from ldap3 import Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("use opv2")

ldap_server = Server("172.16.0.16")


def create_app():
    app = Flask(__name__)
    app.secret_key = "very secret key"

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/opv2"
    app.config["SESSION_TYPE"] = "sqlalchemy"
    db = SQLAlchemy(app)
    app.config["SESSION_SQLALCHEMY"] = db
    server_session = Session(app)
    app.permanent_session_lifetime = datetime.timedelta(minutes=30)
    db.create_all()

    flask_cache_control = FlaskCacheControl()
    flask_cache_control.init_app(app)

    app.config.update(
        SESSION_USE_SIGNER=True,
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax'
    )

    Asset(app)

    from opv2.admin.routes import admin
    from opv2.user.routes import user
    from opv2.login_api.routes import login_api
    from opv2.errors.routes import errors
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(login_api)
    app.register_blueprint(errors)

    return app


def create_firma_token(expires_sec=1800):
    exp = int((datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=expires_sec)).timestamp())
    iat = int((datetime.datetime.now(tz=datetime.timezone.utc)).timestamp())
    token = jwt.encode({"pridat_firmu": True, "exp": f'{exp}', "iat": f'{iat}'},
                       create_app().config['SECRET_KEY'],
                       algorithm="HS256"
                       )
    mycursor.execute(f"insert into tokens values ('{token}')")
    mydb.commit()
    return token


def verify_firma_token(token):
    mycursor.execute(f"select * from tokens where token=%s", (token,))
    verify = mycursor.fetchone()
    if verify is None:
        return False
    try:
        decoded = jwt.decode(token,
                             create_app().config['SECRET_KEY'],
                             algorithms=["HS256"],
                             )
    except jwt.ExpiredSignatureError:
        return False
    return decoded["pridat_firmu"]
