import requests

def ask_question(question, server, timeout=5):
	r = requests.get('%s?q=%s'%(server, question), timeout)
	if r.ok:
		return r.text
	return None