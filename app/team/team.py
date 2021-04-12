from flask import Blueprint, jsonify
from basketball_reference_scraper.seasons import get_standings
from basketball_reference_scraper.teams import get_roster
from basketball_reference_scraper.injury_report import get_injury_report

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
    team_roster = get_roster(team="MIL", season=2021) #team abbv to config, season to os
    roster_list = []
    for row in range(len(team_roster)):
        player = {
            "name": team_roster.loc[row, "PLAYER"],
            "pos": team_roster.loc[row, "POS"],
            "number": int(team_roster.loc[row, "NUMBER"]),
            "exp": team_roster.loc[row, "EXPERIENCE"]
        }
        roster_list.append(player)
    return jsonify({
        "status": 200,
        "message": "OK",
        "query": roster_list
    })

@team_bp.route("/injury")
def get_injury():
    injury_report = (get_injury_report()
                        .query("TEAM == 'MIL'")
                        .reset_index(drop=True)                    
    )
    injury_list = []
    for row in range(len(injury_report)):
        player = {
            "name": injury_report.loc[row, "PLAYER"],
            "injury": injury_report.loc[row, "INJURY"],
            "desc": injury_report.loc[row, "DESCRIPTION"],
            "status": injury_report.loc[row, "STATUS"]
        }
        injury_list.append(player)
    return jsonify({
        "status": 200,
        "message": "OK",
        "query": injury_list
    })