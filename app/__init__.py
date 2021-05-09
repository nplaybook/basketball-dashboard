import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.player import player_bp

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]
app.register_blueprint(player_bp, url_prefix="/players")

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()