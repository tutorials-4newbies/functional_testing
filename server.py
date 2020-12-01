from flask import Flask, url_for, request, json, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy

from config import Config


def init_db(app):
    if not hasattr(app, 'db'):
        app.db = SQLAlchemy(app)


def create_app(app_config: Config):
    app = Flask(__name__, static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_db(app)
    db = app.db

    @app.route('/howdy', methods=['GET'])
    def howdy():
        return "howdy"

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})

    return app


# We might do something else in production

if __name__ == "__main__":
    dev_config = Config()

    app = create_app(dev_config)
    app.run(port=5050, host='127.0.0.1')
