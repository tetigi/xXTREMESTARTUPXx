from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def def_name():
    return 'startupy'

def user_reply(msg):
    print ''
    print '######################'
    print '# UNMATCHED MESSAGE! #'
    print '######################'
    print ''
    print msg
    print 'Please pass input:'
    return raw_input()

questions = { }

@app.route("/")
def answer():
    q = request.args.get("q", "")
    print q
    a = answer_question(q)
    if a is None:
        return user_reply(q)
    else:
        return a

def answer_question(q):
    for regex in questions:
        m = re.search(regex, q)
        if m and m.groups():
            return str(questions[regex](m.groups()))
        elif m:
            return str(questions[regex]())
    return None

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9876, debug=True)
