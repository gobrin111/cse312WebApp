from flask import Blueprint, render_template, send_from_directory, make_response, request
from pymongo import MongoClient
import hashlib

root_bp = Blueprint("root", __name__)

mongo_client = MongoClient("mongo")
db = mongo_client["wurdle"]
user_collection = db["users"]
chat_collection = db["chat"]
like_collection = db["like"]


@root_bp.route("/")
def index():
    auth_token = request.cookies.get('auth_token')
    user = None
    if auth_token:
        user = user_collection.find_one({"auth_token": hashlib.sha256(auth_token.encode('utf-8')).hexdigest()})

    username = user["username"] if user else None

    response = make_response(render_template("index.html", username=username))
    response.headers.set("Content-Type", "text/html")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/login.html")
def login_html():
    response = make_response(render_template("login.html"))
    response.headers.set("Content-Type", "text/html")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/register.html")
def register_html():
    response = make_response(render_template("register.html"))
    response.headers.set("Content-Type", "text/html")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/static/css/style.css")
def css():
    response = make_response(send_from_directory("static/css", "style.css"))
    response.headers.set("Content-Type", "text/css")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/static/css/credentials.css")
def credentials_style():
    response = make_response(send_from_directory("static/css", "credentials.css"))
    response.headers.set("Content-Type", "text/css")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/static/js/script.js")
def js():
    response = make_response(send_from_directory("static/js", "script.js"))
    response.headers.set("Content-Type", "text/javascript")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/static/js/wordFlip.js")
def wordFlip_js():
    response = make_response(send_from_directory("static/js", "wordFlip.js"))
    response.headers.set("Content-Type", "text/javascript")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/static/images/wordle-favicon.ico")
def favicon():
    response = make_response(send_from_directory("static/images", "wordle-favicon.ico"))
    response.headers.set("Content-Type", "image/x-icon")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response


@root_bp.route("/static/images/logo.png")
def image():
    response = make_response(send_from_directory("static/images", "logo.png"))
    response.headers.set("Content-Type", "image/png")
    response.headers.set("X-Content-Type-Options", "nosniff")
    return response
