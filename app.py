from flask import Flask,jsonify,request,render_template
import json
import numpy as np
import os.path
from pathlib import Path

app = Flask(__name__,static_url_path='/static')


@app.route("/")
def home():
	return render_template('login.html')


@app.route('/sign_up',methods=['POST'])
def signup():
	em=request.form["email"]
	pas=request.form["password"]
	x = [em,pas]
	my=Path("details.npy")
	if my.exists():
		y = np.load('details.npy')
		y = y.tolist()
		if x in y:
			return jsonify(0)
		else:
			y.append(x)
			np.save("details",y)
	else:
		np.save("details",x)

	return jsonify(1)


@app.route('/logi',methods=['POST'])
def logi():
	em=request.form["email"]
	pas=request.form["password"]

	par=[em,pas]
	y = np.load('details.npy')
	y=y.tolist()
	print(par)
	if par in y:
		return jsonify(1)
	else :
		return jsonify(0)


	return jsonify(em+pas)

@app.route("/signup")
def signupp():
	return render_template('SignUp.html')

@app.route("/new_page")
def new_page():
	return render_template('new_page.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=233)
 

