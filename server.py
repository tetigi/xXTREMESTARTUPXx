from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("q", "")

    print q

    leader_ans = None

    # while not leader_ans:
        # leader = leaderboard.get_best_ip()
        # leader_ans = crowdsourcer.ask_question(leader, q)

    return "team_kickstarter" # leader_ans

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9876, debug=True)
