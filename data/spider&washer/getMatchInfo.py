import json
import os
from concurrent.futures import ThreadPoolExecutor

import requests

import requestparams

league_ids = []
base_league_url = "https://prod.comp.smoba.qq.com/leaguesite/matches/open"
base_match_url = "https://prod.comp.smoba.qq.com/leaguesite/match/battles/open"
base_battle_url = "https://prod.comp.smoba.qq.com/leaguesite/battle/open"


def getLeagueInfo():
    with open("leagues.json", "r") as file:
        datas = json.load(file)
    for legue in datas.get("results"):
        if legue.get("league_type_name") == "kpl":
            league_ids.append(legue.get("league_id"))

    for league_id in league_ids:
        payload = {'league_id': league_id}
        response = requests.get(base_league_url, headers=requestparams.headers, params=payload)
        datas = response.json()
        dst = f"match/league_info/{league_id}.json"
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, mode="w", encoding="utf-8") as file:
            json.dump(datas, file, ensure_ascii=False)


def getMatchInfo(league_id):
    with open(f"match/league_info/{league_id}.json", "r") as file:
        datas = json.load(file)
    match_ids = []
    for match in datas.get("results"):
        match_ids.append(match.get("match_id"))

    for match_id in match_ids:
        print(f"Processing {match_id}")
        payload = {'match_id': match_id}
        response = requests.get(base_match_url, headers=requestparams.headers, params=payload)
        datas = response.json()
        for battle in datas.get("results"):
            battle_id = battle.get("battle_id")
            payload = {'battle_id': battle_id}
            responses = requests.get(base_battle_url, headers=requestparams.headers, params=payload)
            datass = responses.json()
            dst = f"match/match_info/{match_id}/{battle_id}.json"
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, mode="w", encoding="utf-8") as file:
                json.dump(datass, file, ensure_ascii=False)


if __name__ == "__main__":
    getLeagueInfo()
    with ThreadPoolExecutor(len(league_ids)) as t:
        for league_id in league_ids:
            t.submit(getMatchInfo, league_id)
