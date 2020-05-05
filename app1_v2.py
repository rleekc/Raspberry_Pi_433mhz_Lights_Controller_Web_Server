from flask import Flask
from flask import render_template, Response
from flask import request, redirect,url_for
import os

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def button():
	global state
	error = None
	if request.method == 'POST':
		if (request.form['password'] == 'on'):
			error = "The Lights are on!"
			os.system("~/codesend 6104577")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == 'off'):
			error = "The Lights are off!"
			os.system("~/codesend 6104579")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '0.5H'):
			error = "The Lights are set to 0.5H!"
			os.system("~/codesend 6104580")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '1H'):
			error = "The Lights are set to 1H!"
			os.system("~/codesend 6104582")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '2H'):
			error = "The Lights are set to 2H!"
			os.system("~/codesend 6104583")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '4H'):
			error = "The Lights are set to 4H!"
			os.system("~/codesend 6104585")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '25%'):
			error = "The Lights are set to 25% brightness!"
			os.system("~/codesend 6104586")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '50%'):
			error = "The Lights are set to 50% brightness!"
			os.system("~/codesend 6104588")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '75%'):
			error = "The Lights are set to 75% brightness!"
			os.system("~/codesend 6104589")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == '100%'):
			error = "The Lights are set to 100% brightness!"
			os.system("~/codesend 6104591")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == 'Dim -'):
			error = "The Lights are slightly dimmer!"
			os.system("~/codesend 6104592")		
			return render_template('form_v2.html',error=error)
		if (request.form['password'] == 'Dim +'):
			error = "The Lights are slightly brighter!"
			os.system("~/codesend 6104594")		
			return render_template('form_v2.html',error=error)

	return render_template('form_v2.html', error=None)


	
app.run(port=5000,host="0.0.0.0",threaded=True)
