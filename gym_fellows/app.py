from flask import Flask, request, render_template
from models import Person
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://baliks:password123@localhost/flask_gym'
database_connection = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.form:
		person = Person(username=request.form.get('username'), password=request.form.get('password'))
		database_connection.session.add(person)
		database_connection.session.commit()
	
	# just for proof of concept, show the saved persons
	people = Person.query.all()	
	print(people)
	
	return render_template('signup.html', people=people)
	
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	message = 'Please login with your username and password'
	if request.form:
		person = Person.query.filter_by(username=request.form.get('username'), password=request.form.get('password'))
		person = person.first()
		if person == None:
			message = 'No user found'
		else:
			message = 'Your credentials are validated' 
	
	return render_template('login.html', login_message=message)

	

if __name__ == "__main__":
	app.run(debug=True, port=8080)
