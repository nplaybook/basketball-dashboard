import time
from flask import Blueprint, jsonify
from basketball_reference_scraper.players import get_stats
from basketball_reference_scraper.teams import get_roster

player_bp = Blueprint(name="player_bp", import_name=__name__)

@player_bp.route("/career", methods=["GET"])
def get_player_stats():
    start = time.time()
    try:
        player = get_stats(name="Zach LaVine", stat_type="PER_GAME", playoffs=False, career=True)
    except:
        return jsonify({
            "status": 505,
            "message": "Fail fetch player information"
        })
    else:
        player_stats = {
            "ppg": round(player["PTS"].mean(),1),
            "apg": round(player["AST"].mean(),1),
            "rpg": round(player["TRB"].mean(),1),
            "spg": round(player["STL"].mean(),1),
            "bpg": round(player["BLK"].mean(),1),
            "tov": round(player["TOV"].mean(),1),
            "pf": round(player["PF"].mean(),1)
        }
        return jsonify({
            "status": 200,
            "message": "OK",
            "execution_time": f"{round(time.time() - start, 2)} s",
            "query": player_stats
            })

@player_bp.route("/bio", methods=["GET"])
def get_player_bio():
    try:
        team_roster = get_roster(team="CHI", season=2021)
    except:
        return jsonify({
            "status": 505,
            "message": "Fail fetch player information"
        })
    else:
        player_info = team_roster.query("PLAYER == 'Zach LaVine'")
        player_info = {
            "name": player_info["PLAYER"].values[0],
            "jersey": int(player_info["NUMBER"].values[0]),
            "pos": player_info["POS"].values[0],
            "height": player_info["HEIGHT"].values[0],
            "weight": int(player_info["WEIGHT"].values[0]),
            "experience": int(player_info["EXPERIENCE"].values[0])
        }
        return jsonify({
            "status": 200,
            "message": "OK",
            "query": player_info
        })