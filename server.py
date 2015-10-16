from flask import Flask, request, jsonify
import re

# Modules
import mods.reverse
import mods.arithmetic
import mods.sum_elements
import mods.fib
import mods.earliest
import mods.max_element
import mods.romanNumeralsCalculator

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

def dumb_str(xs):
    return 'no'

def dumb_int(xs):
    return 0

questions = {
        'Convert (\d+) into Roman Numerals': mods.romanNumeralsCalculator.romanNumerals,
        'What is ([IXV]+) in decimal': mods.romanNumeralsCalculator.romanToDecimal,
        'what is (\d+) plus (\d+)': mods.arithmetic.plus,
        'Find 2 elements that sum to 0 in: (.+)': mods.sum_elements.sum_two_elements_to_zero,
        'which of the following numbers is the largest: (.*)': mods.max_element.max_element,
        'what is the (\d+)(th|nd|st) number in the Fibonacci sequence': mods.fib.fib,
        'which of the following is earliest: (.*)': mods.earliest.whichIsEarliest,
        'what is (\d+) multiplied by (\d+)': mods.arithmetic.multiply,
        'which of the following is an anagram of \"(\w+)\"': dumb_str,
        'what is the english scrabble score of (\w+)': dumb_int
        }

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
