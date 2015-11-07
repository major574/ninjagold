from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'whatever'
@app.route('/')
def index():
	try:
		session['gold']
	except:
		session['gold'] = 0
	try:
		session['message']
	except:
		session['message'] = []
	return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def gold():
	if request.form['roll'] == "farmval":
		val = random.randrange(10,20)
	if request.form['roll'] == "caveval":
		val = random.randrange(5,10)
	if request.form['roll'] == "houseval":
		val = random.randrange(2,5)
	elif request.form['roll'] == "casinoval":
		val = random.randrange(-50,50)
	session['gold'] += val
	session['message'].append(val) 
	return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
	session.pop('gold')
	session.pop('message')
	return redirect('/')	
app.run(debug=True)