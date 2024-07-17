from flask import Flask, render_template
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

@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/fortune')
def fortune():
	rand_option = random.randint(0,9)
	return render_template("fortune.html", option=fortune_options[rand_option])

if __name__ == '__main__':
    app.run(debug=True)