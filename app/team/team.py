from flask import Blueprint, jsonify
from basketball_reference_scraper.seasons import get_standings
from basketball_reference_scraper.teams import get_roster
# from basketball_reference_scraper.injury_report import get_injury_report

team_bp = Blueprint(name="team_bp", import_name=__name__)

@team_bp.route("/standing")
def standing():
    current_standing = get_standings()["Eastern Conference"]
    current_standing = (current_standing
                            .query("`Eastern Conference` == 'Milwaukee Bucks'") # team name to config
                            .reset_index(drop=False)
                        )

    return jsonify({ 
        "status": 200,
        "message": "OK",
        "query": {
                "position": int(current_standing.loc[0, "index"]+1),
                "win": int(current_standing.loc[0, "W"]),
                "lose": int(current_standing.loc[0, "L"]),
                "percentage": float(current_standing.loc[0, "W/L%"]),
                "game_back": float(current_standing.loc[0, "GB"])
                # add upcoming game schedule
            } 
        })

@team_bp.route("/roster")
def roster():
    # python versioning issue and result runtime error, please downgrade 
    team_roster = get_roster(team="MIL", season=2021) #team abbv to config, season to os
    print(team_roster)
    return "OK"

# @team_bp.route("/injury")
# def get_injury():
#     injury_report = get_injury_report()
#     try:
#         print(injury_report.columns)
#     except:
#         print(injury_report.keys())
#     return "OK"