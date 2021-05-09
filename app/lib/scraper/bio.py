import requests
from typing import Optional
from bs4 import BeautifulSoup

def get_bio(url: str) -> Optional[dict]:
    """This function is used to get player's biodata"""

    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    meta = soup.find("div", { "id": "meta" })
    
    # height and weight
    height, weight = meta.findAll("span", { "itemprop": ["height", "weight"] })
    height = height.contents[0]
    weight = weight.contents[0]

    # birth data
    birth_date = meta.findAll("span", { "itemprop": "birthDate" })[0]
    birth_date = birth_date.attrs["data-birth"]

    # draft
    meta_p = meta.findAll("p")
    try:
        for index in range(len(meta_p)):
            if "Draft" in meta_p[index].getText():
                draft_detail = meta_p[index]
                round_, pick = draft_detail.getText().split(', ')[1].split(' (')
                team, year = draft_detail.findAll("a")
                team = team.contents[0]
                year = year.contents[0].split()[0]
                break
    except Exception as e:
        print(e)
        return None
    else:
        return {
            "height": height,
            "weight": weight,
            "birthDate": birth_date,
            "draftRound": round_,
            "draftPick": pick,
            "draftTeam": team,
            "draftYear": year
        }