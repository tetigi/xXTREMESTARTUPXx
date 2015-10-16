import requests

def ask_question(question, ip, timeout=5):
	r = requests.get('http://%s?q=%s'%(ip, question), timeout)
	if r.ok:
		return r.text
	return None