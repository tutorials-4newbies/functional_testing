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

    class BucketWish(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @app.route('/howdy', methods=['GET'])
    def howdy():
        return "howdy"

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})

    @app.route("/goodbye/<name>")
    def goodbye(name: str):
        answer = f"goodbye Mr {name}"
        return jsonify({"response": answer})

    @app.route("/bucket_list", methods=["GET", "POST"])
    def bucket_list():
        if request.method == "POST":
            pass
            # write logic, probably using the data from request.get_json()
            # Note you'll need to send data with the correct headers (Content-Type: application/json)
            # and the data in the body
        else:
            pass
            # write GET logic

    return app


# We might do something else in production

if __name__ == "__main__":
    dev_config = Config()

    flask_app = create_app(dev_config)
    flask_app.run(port=5050, host='127.0.0.1')
