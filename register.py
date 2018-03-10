#pylint:disable=print-statement

from flask import Flask,render_template,request,redirect,session,flash  # Import Flask to allow us to create our app.
import re, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
app.secret_key = 'ThisIsSecret'                        # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def starter():
    return render_template('index.html')  
  
@app.route('/results', methods=['POST'])
def results():
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['password_confirmation']) < 1:
        flash("You must fill out all fields!",'error')
    if len(request.form['password']) < 8:
        flash("Password must exceed 8 characters!",'error')
    if any(char.isdigit() for char in request.form['first_name']) == True or any(char.isdigit() for char in request.form['last_name']) == True:
        flash("Name cannot contain any numbers!",'error')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!",'error')
    if request.form['password'] != request.form['password_confirmation']:
        flash("Password and confirmation must match!",'error')
    if re.search(r"[A-Z]", request.form['password']) is None or re.search(r"[a-z]", request.form['password']) is None or re.search(r"\d", request.form['password']) is None:
        flash("Passwords must have at least 1 number, 1 lowercase letter, and 1 uppercase letter!",'error')
    if datetime.datetime.now().isoformat() <= request.form['birthday']:
        flash("Begone, time traveler!",'error')    
    flash("Thank you for registering!")
    return redirect('/')
app.run(debug=True)      # Run the app in debug mode.