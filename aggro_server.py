import crowdsourcer
import team_finder
import time
import random

RANDOM_QUESTIONS = [
    "What number am I thinking of?",
    "Who is better? Joe, Huw or Callum?",
    "To successfully answer this question, please restart your server.",
    "Who is Luke's father?",
    "How tall is Huw?",
    "What is 1 plus 1?",
    "What is 0 really?",
    "How much wood could a woodchuck chuck if a wood chuck could chuck wood?",
    "Which position is your team in?"
    "What is your score?",
    "FDE or Dev?",
    "What is the meaning of life?",
    "What is FRP?",
    "Which has been the best session so far?",
    "Karp or Thiel?"
]

def get_random_question():
    return random.choice(RANDOM_QUESTIONS)

if __name__ == "__main__":
    while True:
        time.sleep(0.1)
        teams = team_finder.get_ranked_teams('http://192.168.3.32:3000/', 'team_kickstarter')
        random_team = random.choice(teams)
        leader_ans = crowdsourcer.ask_question(q, random_team.url)
        try:
            print "Asking " + str(q) + " to " + random_team.team
            q = get_random_question()
            print "Received " + str(leader_ans)
        except Exception as e:
            print "Failed to ask " + str(random_team.team) + " question " + str(q) + ". Got exception " + str(e)

