def score(participant):
    return participant["chickenwings"] * 5 + participant["hamburgers"] * 3 + participant["hotdogs"] * 2

def create_scoreboard(participants):
    scoreboard = []
    for participant in participants:
        scoreboard.append({"name": participant["name"], "score":score(participant)})
    scoreboard.sort(key=lambda x: (-x["score"], x["name"]))
    return scoreboard


participants = [
  {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
  {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

scoreboard = create_scoreboard(participants)
print(scoreboard)