from flask_sqlalchemy import SQLAlchemy
from app import app
from datetime import datetime

db = SQLAlchemy(app)

class Position(db.Model):
    __tablename__ = "Positions"
    
    position_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    positions = db.relationship("Player", backref="Position", lazy=True)

    def __init__(self, name, create_date):
        self.name = name
        self.create_date = create_date

class Player(db.Model):
    __tablename__ = "Players"
    
    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey("Position.position_id"), nullable=False)
    height = db.Column(db.String(8))
    weight = db.Column(db.Float())
    experience_year = db.Column(db.Integer)
    jersey_number = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)
    create_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    update_date = create_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    # players = 

    def __init__(self, name, position_id, height, weight, experience_year, jersey_number, is_active, create_date, update_date):
        self.name = name
        self.position_id = position_id
        self.height = height
        self.weight = weight
        self.experience_year = experience_year
        self.jersey_number = jersey_number
        self.is_active = is_active
        self.create_date = create_date
        self.update_date = update_date

class TradStats(db.Model):
    __tablename__ = "TraditionalStatistics"
    
    traditional_statistics_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey("Player.player_id"), nullable=False)
    season = db.Column(db.Integer)
    game_played = db.Column(db.Integer)
    game_started = db.Column(db.Integer)
    minute_play = db.Column(db.Float)
    field_goal_made = db.Column(db.Integer)
    field_goal_attemp = db.Column(db.Integer)
    field_goal_percentage = db.Column(db.Float)
    three_point_made = db.Column(db.Integer)
    three_point_attemp = db.Column(db.Integer)
    three_point_percentage = db.Column(db.Float)
    two_point_made = db.Column(db.Integer)
    two_point_attemp = db.Column(db.Integer)
    two_point_percentage = db.Column(db.Float)
    effective_field_goal = db.Colunn(db.Float)
    free_throw_made = db.Column(db.Integer)
    free_throw_attemp = db.Column(db.Integer)
    free_throw_percentage = db.Column(db.Float)
    offensive_rebound = db.Column(db.Float)
    defensive_rebound = db.Column(db.Float)
    total_rebound = db.Column(db.Float)
    assist = db.Column(db.Float)
    steal = db.Column(db.Float)
    block = db.Column(db.Float)
    turnover = db.Column(db.Float)
    personal_foul = db.Column(db.Float)
    points = db.Column(db.Float)
    create_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, player_id, season, game_played, game_started, minute_play, field_goal_made, field_goal_attemp, field_goal_percentage, 
    three_point_made, three_point_attemp, three_point_percentage, two_point_made, two_point_attemp, two_point_percentage, effective_field_goal,
    free_throw_made, free_throw_attemp, free_throw_percentage, offensive_rebound, defensive_rebound, total_rebound, assist, steal, block, turnover,
    personal_foul, points):

        self.player_id = player_id
        self.season = season
        self.game_played = game_played 
        self.game_started = game_started
        self.minute_play = minute_play 
        self.field_goal_made = field_goal_made
        self.field_goal_attemp = field_goal_attemp
        self.field_goal_percentage = field_goal_percentage 
        self.three_point_made = three_point_made
        self.three_point_attemp = three_point_attemp
        self.three_point_percentage = three_point_percentage
        self.two_point_made = two_point_made
        self.two_point_attemp = two_point_attemp
        self.two_point_percentage = two_point_percentage
        self.effective_field_goal = effective_field_goal
        self.free_throw_made = free_throw_made
        self.free_throw_attemp = free_throw_attemp
        self.free_throw_percentage = free_throw_percentage
        self.offensive_rebound = offensive_rebound
        self.defensive_rebound = defensive_rebound
        self.total_rebound = total_rebound
        self.assist = assist
        self.steal = steal
        self.block = block
        self.turnover = turnover
        self.personal_foul = personal_foul
        self.points = points

class AdvStats(db.Model):
    __tablename__ = "AdvanceStatistics"
    
    advance_statistics_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey("Player.player_id"), nullable=False)
    season = db.Column(db.Integer)
    player_efficiency = db.Column(db.Float)
    true_shooting_percentage = db.Column(db.Float)
    three_point_attemp_rate = db.Column(db.Float)
    free_throw_attemp_rate = db.Column(db.Float)
    offensive_rebound_percentage = db.Column(db.Float)
    defensive_rebound_percentage = db.Column(db.Float)
    total_rebound_percentage = db.Column(db.Float)
    assist_percentage = db.Column(db.Float)
    steal_percentage = db.Column(db.Float)
    block_percentage = db.Column(db.Float)
    turnover_percentage = db.Column(db.Float)
    usage_percentage = db.Column(db.Float)
    offensive_win_share = db.Column(db.Float)
    defensive_win_share = db.Column(db.Float)
    win_share = db.Column(db.Float)
    win_share_per_48 = db.Column(db.Float)
    offensive_box_plus_minus = db.Column(db.Float)
    defensive_box_plus_minus = db.Column(db.Float)
    box_plus_minus = db.Column(db.Float)
    create_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, player_id, season, player_efficiency, true_shooting_percentage, three_point_attemp_rate, free_throw_attemp_rate, 
    offensive_rebound_percentage, defensive_rebound_percentage, total_rebound_percentage, assist_percentage, steal_percentage, block_percentage, 
    turnover_percentage, usage_percentage, offensive_win_share, defensive_win_share, win_share, win_share_per_48, offensive_box_plus_minus, 
    defensive_box_plus_minus, box_plus_minus):

        self.player_id = player_id
        self.season = season
        self.player_efficiency = player_efficiency
        self.true_shooting_percentage = true_shooting_percentage
        self.three_point_attemp_rate = three_point_attemp_rate
        self.free_throw_attemp_rate = free_throw_attemp_rate,
        self.offensive_rebound_percentage = offensive_rebound_percentage
        self.defensive_rebound_percentage = defensive_rebound_percentage
        self.total_rebound_percentage = total_rebound_percentage
        self.assist_percentage = assist_percentage
        self.steal_percentage = steal_percentage
        self.block_percentage = block_percentage
        self.turnover_percentage = turnover_percentage
        self.usage_percentage = usage_percentage
        self.offensive_win_share = offensive_win_share
        self.defensive_win_share = defensive_win_share
        self.win_share = win_share
        self.win_share_per_48 = win_share_per_48
        self.offensive_box_plus_minus = offensive_box_plus_minus
        self.defensive_box_plus_minus = defensive_box_plus_minus
        self.box_plus_minus = box_plus_minus

class ShootHistory(db.Model):
    __tablename__ = "ShootHistory"
    
    shoot_history_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey("Player.player_id"), nullable=False)
    # season = db.Column(db.Integer)
    loc_x = db.Column(db.Float, nullable=False)
    loc_y = db.Column(db.Float, nullable=False)
    distance = db.Column(db.Integer)
    make_miss = db.Column(db.Boolean)
    value = db.Column(db.Integer)
    quarter = db.Column(db.Integer)
    game_date = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)

    def __init__(self, player_id, loc_x, loc_y, distance, make_miss, value, quarter, game_date):
        self.player_id = player_id
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.distance = distance
        self.make_miss = make_miss
        self.value = value
        self.quarter = quarter
        self.game_date = game_date

class GameSchedule(db.Model):
    __tablename__ = "GameSchedule"

    opponent_team = db.Column(db.String(32), nullable=False)
    game_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, opponent_team, game_date):
        self.opponent_team = opponent_team
        self.game_date = game_date

db.create_all()