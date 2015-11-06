from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'whatever'
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def gold():
	# try:
	# 	session['roll']
	# except:
	# 	session['roll'] = random.randrange(20,50)
	if request.form['roll'] == "farmval":
		print "heres some farm"
	elif request.form['roll'] == "caveval":
		print "heres some cave"
	elif request.form['roll'] == "houseval":
		print "heres some house"
	elif request.form['roll'] == "casinoval":
		print "heres some casino"
	return redirect('/')
app.run(debug=True)