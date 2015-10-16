from flask import Flask, request, jsonify

import crowdsourcer
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
        # leader = "http://192.168.3.39:3000" # leaderboard.get_best_ip()
        leader = "http://192.168.3.35:1337" # leaderboard.get_best_ip()
        print "The leader is: " + str(leader)
        leader_ans = crowdsourcer.ask_question(q, leader)
        print "They replied with: " + str(leader_ans)

    return leader_ans

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9876, debug=True)
