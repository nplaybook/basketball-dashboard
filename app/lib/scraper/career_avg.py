import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_career_avg(
    url: str, 
    stat_type: str="PER_GAME", 
    playoff: bool=False, 
    career: bool=True
    ) -> pd.DataFrame:
    """This function is used to get player's career average.
    
    param: url - player's url from database
    param: stat_type - options are PER_GAME, PER_MINUTE, PER_POSS, ADVANCED
    param: playoff - if True, show only career average for playoffs
    param: career - if False, show all season average. If True, group season average per team 

    Scraper inspired by: https://github.com/vishaalagartha/basketball_reference_scraper
    """

    selector = stat_type.lower()
    if playoff:
        selector = "playoffs_" + selector
    df = get_table(url=url selector=selector)
    df = df.query("Season == 'Career'")
    df = df.dropna(axis=1)
    return df

def get_table(
    url: str, 
    selector: str
    ) -> pd.DataFrame:
    """This function is used to scrape table from basketball-reference.com"""

    r = requests.get(f"https://www.basketball-reference.com/{url}")
    soup = BeautifulSoup(r.text, features="lxml")
    table = soup.select(selector=f"#{selector}")
    return pd.read_html(str(table))[0]