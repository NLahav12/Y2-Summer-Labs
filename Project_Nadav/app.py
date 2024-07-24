from flask import Flask, render_template,url_for,redirect,request, session 
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCNi5X96FmEfAIGQUg894stvO2BTeGfgsI",
  'authDomain': "nadavinividualproject.firebaseapp.com",
  'projectId': "nadavinividualproject",
  'storageBucket': "nadavinividualproject.appspot.com",
  'messagingSenderId': "945126126248",
  'appId': "1:945126126248:web:ab995a8675185c0c0c489d",
  'databaseURL':"https://nadavinividualproject-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "Nadav"


@app.route('/', methods = ['GET', 'POST'])
def start():
    return render_template("start.html")

@app.route('/sign-in', methods=['GET','POST'])
def signIn():
    if request.method == 'POST':
    	email = request.form['email']
    	password = request.form['password']
    	session['user'] = auth.sign_in_with_email_and_password(email, password)
    	user_id = session['user']['localId']
    	t = db.child('user_task_list').child(user_id).child('task').get().val()
    	return render_template('display_list.html', tasks=t)

    return render_template("signIn.html")

@app.route('/sign-up', methods = ['GET', 'POST'])
def signUp():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		username = request.form['username']
		user = {'email' : email, 'username': username, 'task':{}}
		session['user'] = auth.create_user_with_email_and_password(email, password)
		db.child('user_task_list').child(session['user']['localId']).set(user)
		return render_template('display_list.html',tasks=user['task'])

	return render_template("signUp.html")

@app.route('/display-users-list', methods = ['GET', 'POST'])
def display_list():
	if 'user' not in session:
		return redirect(url_for('signIn'))

	user_id = session['user']['localId']
	tasks = db.child('user_task_list').child(user_id).child('task').get().val()

	if request.method == 'POST':
		task_action = request.form.get('task_action')
		task_description = request.form.get('task_description')
		task_id = request.form.get('task_id')

		if task_action == 'add' and task_description:
			db.child('user_task_list').child(user_id).child('task').push(task_description)
		elif task_action == 'remove' and task_id:
			db.child('user_task_list').child(user_id).child('task').child(task_id).remove()
		elif task_action == 'update' and task_id and task_description:
			db.child('user_task_list').child(user_id).child('task').child(task_id).set(task_description)
		return redirect(url_for('display_list'))

	return render_template("display_list.html", tasks=tasks)

@app.route('/logout')
def logout():
	session.pop('user', None)
	return redirect(url_for('start'))


if __name__ == '__main__':
	app.run(debug=True) 
