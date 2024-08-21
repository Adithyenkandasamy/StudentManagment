from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route("/")
def index():
    return redirect("/login")
# Home Page - Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        # Check if user already exists
        existing_user = Student.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please try a different one.")
            return redirect(url_for('register'))

        # Create new user
        new_user = Student(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Student.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('student_details'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))

    return render_template('login.html')

# Student Details Page
@app.route('/student_details', methods=['GET', 'POST'])
def student_details():
    if 'user_id' not in session:
        flash('You must log in to view this page.')
        return redirect(url_for('login'))

    user_id = session['user_id']
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']

        # Check if student details already exist
        existing_details = StudentDetail.query.filter_by(user_id=user_id).first()
        if existing_details:
            flash('You have already submitted your details.')
            return redirect(url_for('student_details'))

        # Add student details
        student_details = StudentDetail(name=name, email=email, phone=phone, course=course, user_id=user_id)
        db.session.add(student_details)
        db.session.commit()

        flash('Details submitted successfully!')
        return redirect(url_for('student_details'))

    return render_template('student_details.html')

# Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Creates the database tables
    app.run(debug=True)
