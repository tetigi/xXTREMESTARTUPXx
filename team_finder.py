from BeautifulSoup import BeautifulSoup
import urllib2
import HTMLParser
import sys
import re

TEAM_REGEX = '(.*)\s+\((http://.*)\)'

class TeamScore:
    def __init__(self, team, score):
        parsed = re.search(TEAM_REGEX, team)
        if(parsed):
            self.team = parsed.group(1)
            self.url = parsed.group(2)
        else:
            self.team = "Unknown"
            self.url = "Unknown"
        self.score = score

    def __str__(self):
        return "Team: " + str(self.team) + ", url: " + str(self.url) + ", score: " + str(self.score)



def load_players(url):
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)

    list_players = soup.findAll('li', {'class': 'player'})

    players = []
    h = HTMLParser.HTMLParser()
    for list_item in list_players:
        player = TeamScore(list_item.find('div', {'class': 'ranking name'}).getText(), list_item.find('div', {'class': 'ranking points'}).getText())
        players.append(player)

    return players

def ignore_team(players, ignore):
    new_players = []
    for player in players:
        if(player.team != ignore):
            new_players.append(player)

    return new_players

def compare(team1, team2):
    return (team1.score < team2.score)

def sort_players(players):
    return sorted(players, cmp=compare)

def get_best_team(url, ignore):
    sorted_players = get_ranked_teams(url, ignore)
    return sorted_players[0]

def get_ranked_teams(url, ignore):
    players = load_players(url)
    filtered_players = ignore_team(players, ignore)
    sorted_players = sort_players(filtered_players)
    return sorted_players

def get_our_score(url, our_team):
    players = load_players(url)
    for player in players:
        if player.team == our_team:
            return player.score
    return None

if __name__ == "__main__":
    url = sys.argv[1]
    ignore = sys.argv[2]

    ranked = get_ranked_teams(url, ignore)

    for player in ranked:
        print str(player)

    print "you should choose: " + str(get_best_team(url, ignore))

    print "our score is: " + str(get_our_score(url, ignore))


