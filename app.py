from os import getenv

from flask import Flask

from routes.chat_routes import chat_bp

app = Flask(__name__, static_folder="templates/static", static_url_path="/static")
app.secret_key = getenv("FLASK_SECRET_KEY", "dev-secret-key")
app.register_blueprint(chat_bp)


if __name__ == "__main__":
    app.run(debug=True)
