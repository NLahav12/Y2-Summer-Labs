from flask import Flask, render_template,url_for,redirect,request, session
import random

app = Flask(__name__, 
template_folder='templates',
static_folder='static')

app.config['SECRET_KEY'] = "NADAV"

fortune_options = [
"rich",
 "sad",
  "happy",
   "married",
    "lonely",
     "mad",
      "smart",
       "in love",
        "hated",
         "crazy"]

@app.route('/')
def start():
    return render_template('start.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return redirect(url_for('start'))
    else:
        session['birthday'] = request.form['birth_date']
        session['name'] = request.form['name']
        return render_template('home.html')


@app.route('/fortune')
def fortune():
	option_choice = len(session['birthday']) % 10
	return render_template("fortune.html", option=fortune_options[option_choice])

if __name__ == '__main__':
    app.run(debug=True)