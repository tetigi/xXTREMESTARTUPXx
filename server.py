from flask import Flask, request, jsonify

import crowdsourcer
import team_finder
import time

app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("q", "")

    print "The question was: " + q

    leader_ans = None

    while not leader_ans:
        print 'Sleeping..'
        time.sleep(2)
        leading_team = team_finder.get_best_team('http://192.168.3.32:3000/', 'team_kickstarter')
        print "The leader is {} with ip: {}".format(leading_team.team, leading_team.url)
        leader_ans = crowdsourcer.ask_question(q, leading_team.url)
        print "They replied with: " + str(leader_ans)

    return leader_ans

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9876, debug=True)
