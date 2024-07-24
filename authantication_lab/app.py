from flask import Flask, render_template,url_for,redirect,request, session 
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyAVeQOFv4PRe45t7PVaOrJO-iA0XSfBs8c",
  "authDomain": "nadav-project-4790d.firebaseapp.com",
  "projectId": "nadav-project-4790d",
  "storageBucket": "nadav-project-4790d.appspot.com",
  "messagingSenderId": "116084454845",
  "appId": "1:116084454845:web:95bf747974c7fb9c474ed4",
  "measurementId": "G-SX997E61VJ",
  "databaseURL": "https://nadav-project-4790d-default-rtdb.europe-west1.firebasedatabase.app"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "Nadav"

@app.route('/', methods = ['GET', 'POST'])
def signUp():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    full_name = request.form['full_name']
    user = {'email' : email, 'username': username, 'full_name': full_name}
    session['user'] = auth.create_user_with_email_and_password(email, password)
    db.child('Users').child(session['user']['localId']).set(user)
    return redirect(url_for('home'))

  return render_template("signup.html")


@app.route('/sign-in', methods=['GET','POST'])
def signIn():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    session['user'] = auth.sign_in_with_email_and_password(email, password)
    return redirect(url_for('home'))

  return render_template("signIn.html")


@app.route('/home', methods = ['GET','POST'])
def home():
  if request.method == 'POST':
    quote = request.form['quote']
    speaker = request.form['speaker']
    session['speaker'] = speaker
    session['quote'] = quote
    quote_info= {'said_by' : speaker,'quote': quote, 'uid' : session['user']['localId']}
    db.child('Quotes').push(quote_info)
    return redirect(url_for('thanks'))
  return render_template('home.html')


@app.route('/display')
def display():
  if session['user'] != None:
    return render_template("display.html", quotes = db.child('Quotes').get().val())
  else:
    return redirect(url_for('signIn'))

@app.route('/thanks')
def thanks():
  if session['user'] != None:
    quote = session['quote']
    speaker = session['speaker']
    return render_template("thanks.html",quote = quote, speaker = speaker)
  else:
    return redirect(url_for('signIn'))

@app.route('/sign-out')
def signOut():
  session['user']=None
  auth.current_user = None
  return redirect(url_for('signIn'))

if __name__ == '__main__':
    app.run(debug=True)
