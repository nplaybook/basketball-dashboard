from flask import Flask

from .team.team import team_bp

app = Flask(__name__)

app.register_blueprint(team_bp, url_prefix="/team")

if __name__ == "__main__":
    app.run()