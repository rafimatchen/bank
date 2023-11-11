import os

from flask import Flask, redirect, request, url_for

from .db import get_db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "server.sql"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.get("/hello")
    def hello():
        return "Hello, world!"

    @app.post("/tdtext")
    def td_text():
        response_content = request.get_json()
        message: str = response_content["message"]
        code = message.split(" ")[2]
        write_code_to_db(code)

    @app.post("/tdcode")
    def td_code():
        response_content = request.get_json()
        code: str = response_content["message"]
        write_code_to_db(code)
        return "200"

    def write_code_to_db(code: str):
        if not code.isnumeric():
            raise ValueError(f"Code {code}\n is non-numeric.")
        db = get_db()

        db.execute("INSERT INTO security_code (code) VALUES (?)", (code,))
        db.commit()

    from . import db

    db.init_app(app)
    return app
