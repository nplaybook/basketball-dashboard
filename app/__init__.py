import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.team.team import team_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:110696@localhost:5432/basketball-dashboard"
app.register_blueprint(team_bp, url_prefix="/team")

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()