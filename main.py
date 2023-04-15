from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

urls = [
    "https://steamcommunity.com/stats/589940/leaderboards/7830035",
    "https://steamcommunity.com/stats/589940/leaderboards/7830015",
    "https://steamcommunity.com/stats/589940/leaderboards/7830025",
    "https://steamcommunity.com/stats/589940/leaderboards/7830029",
    "https://steamcommunity.com/stats/589940/leaderboards/7830034",
    "https://steamcommunity.com/stats/589940/leaderboards/7830012",
    "https://steamcommunity.com/stats/589940/leaderboards/7830019",
    "https://steamcommunity.com/stats/589940/leaderboards/7830041",
    "https://steamcommunity.com/stats/589940/leaderboards/7830028",
    "https://steamcommunity.com/stats/589940/leaderboards/7830014",
    "https://steamcommunity.com/stats/589940/leaderboards/7830022"
]

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # get leaderboard name
    raw = str(soup.select("div#leaderHeader")[0])
    raw = raw.split("<br/>")[1]
    raw = raw.split("</div>")[0]
    leaderboardName = raw.strip()
    print(leaderboardName)

    # get leaderboard entries
    entries = soup.select("div.lbentry")
    if len(entries) > 0:
        data = []
        for e in entries:
            rank = e.select("div.relativeRank")[0].select("div.rR")[0].text
            player = e.select("div.player")[0].select("a.playerName")[0].text
            score = e.select("div.score")[0].text
            data.append([rank, player, score])
        print(tabulate(data, headers = ["Rank", "Player", "Score"]))
        print("\n\n")
    else:
        print("No entries.\n\n")

input("Press enter to quit.")
