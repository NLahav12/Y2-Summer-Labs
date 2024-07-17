from flask import Flask, render_template,url_for,redirect,request
import random

app = Flask(__name__, 
template_folder='templates',
static_folder='static')

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

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        birth_date = request.form['birth_date']
        return redirect(url_for('fortune', bday = birth_date))


@app.route('/fortune/<bday>')
def fortune(bday):
	option_choice = len(bday) % 10
	return render_template("fortune.html", option=fortune_options[option_choice])

if __name__ == '__main__':
    app.run(debug=True)