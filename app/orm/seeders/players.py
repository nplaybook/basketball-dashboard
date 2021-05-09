import json
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from dotenv import load_dotenv
from lib.db.db import DB

def seed():
    """This function is used to seed players name and href data from json dir"""

    load_dotenv()

    db = DB(
        host=os.environ["HOST"],
        db_name=os.environ["DB"],
        username=os.environ["NAME"],
        password=os.environ["PASS"]
    )

    with open('./json/players.json', 'r') as file:
        players_json = file.read()
    players_json = json.loads(players_json)

    query = get_insert_query(data=players_json)
    
    db.execute_query(query=query, flag=2)
    print("OK")

def get_insert_query(data: list):
    """This function is used to generate SQL query for insert data purpose"""

    SCHEMA: str = os.environ["SCHEMA"]
    TABLE: str = os.environ["PLAYERS"]
    COLUMNS: str = '"name", "name_lower", "href", "is_active", "created_at", "updated_at"'
    
    header = f'INSERT INTO "{SCHEMA}"."{TABLE}" ({COLUMNS}) VALUES '
    body: str = ''
    for index in range(len(data)):
        name = data[index]["name"].replace("'", '"')
        lower_name = data[index]["name_lower"].replace("'", '"')
        href = data[index]["href"]
        body += f"""
                ('%s', '%s', '%s', TRUE, current_timestamp, current_timestamp)
                """ % (name, lower_name, href)
        if index != len(data)-1:
            body += ", "
    return header + body

if __name__ == '__main__':
    seed()