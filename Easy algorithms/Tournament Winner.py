"""
Function that returns the winner of the tournament in a given competitions and results where the competitions are an array
that has elements in the form of [home_team, away_team]. The results array contains information about the winner of each
corresponding competition in the competitions array. results[i] denotes the winner of competitions[i], where a 1 in the
results array means that the home_team in the corresponding competition won and a 0 means that the away_team won.
Only one team will win the tournament and that each team will compete against all other teams excatly once.

Sample Input:                  |         Sample Output:
competitions = [               |            Python
    ["HTML", "C#"],            |         # C# beats HTML, Python beats C#, and Python beats HTML
    ["C#", "Python"],          |         # HTML - 0 points
    ["Python", "HTML"]         |         # C# - 3 points
]                              |         # Python - 6 points
results = [0, 0, 1]            |
"""


# O(n) time | O(k) space - where n is the number of competitions and k is the number of teams
def tournament_winner(competitions, results):
    HOME_TEAM_WON = 1
    teams_score = {}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition

        if home_team not in teams_score:
            teams_score[home_team] = 0
        if away_team not in teams_score:
            teams_score[away_team] = 0

        winning_team = home_team if result == HOME_TEAM_WON else away_team
        teams_score[winning_team] += 3

    return sorted(teams_score, key=lambda x: teams_score[x])[-1]


competitions = [
    ["AlgoMasters", "FrontPage Freebirds"],
    ["Runtime Terror", "Static Startup"],
    ["WeC#", "Hypertext Assassins"],
    ["AlgoMasters", "WeC#"],
    ["Static Startup", "Hypertext Assassins"],
    ["Runtime Terror", "FrontPage Freebirds"],
    ["AlgoMasters", "Runtime Terror"],
    ["Hypertext Assassins", "FrontPage Freebirds"],
    ["Static Startup", "WeC#"],
    ["AlgoMasters", "Static Startup"],
    ["FrontPage Freebirds", "WeC#"],
    ["Hypertext Assassins", "Runtime Terror"],
    ["AlgoMasters", "Hypertext Assassins"],
    ["WeC#", "Runtime Terror"],
    ["FrontPage Freebirds", "Static Startup"]
]
results = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
print(tournament_winner(competitions, results))