import requests
import grequests
from urllib2 import urlparse

def ask_question(question, server, timeout=5):
	r = requests.get('%s?q=%s'%(server, question), timeout)
	if r.ok:
		return r.text
	return None

def _netloc(url):
	return urlparse.urlparse(url).netloc

def distribute(question, participants, timeout=5):
	scores = dict([(_netloc(p.url), int(p.score)) for p in participants])
	rs = (grequests.get('%s?q=%s'%(p.url, question), timeout=timeout) for p in participants)
	responses = grequests.map(rs)
	answers = {}
	for r in responses:
		if r.ok:
			answers[r.text] = answers.get(r.text, 0) + scores[_netloc(str(r.url))]
	if answers:
		return sorted(answers.items(), key=lambda x: x[1])[-1][0]
	return None