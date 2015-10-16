from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("q", "")
    print q
    return ":("

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9876, debug=True)
