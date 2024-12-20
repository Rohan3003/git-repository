from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User Model for Authentication
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# SBU Selection Form
class SBUForm(FlaskForm):
    sbu = SelectField('Select Service Business Unit', choices=[('SBU1', 'SBU1'), ('SBU2', 'SBU2')], validators=[DataRequired()])
    submit = SubmitField('Next')

# Project Selection Form
class ProjectForm(FlaskForm):
    project = SelectField('Select Project', choices=[('BMO', 'BMO'), ('RBCCM', 'RBCCM'), ('RBCWM', 'RBCWM'), ('CS', 'CS'), ('MKTX', 'MKTX')], validators=[DataRequired()])
    submit = SubmitField('Next')

# Portfolio Selection Form
class PortfolioForm(FlaskForm):
    portfolio = SelectField('Select Portfolio', choices=[('TES', 'TES'), ('RAMPP', 'RAMPP'), ('CBDDT', 'CBDDT'), ('BCS-T', 'BCS-T'), ('DCM', 'DCM'), ('P&RS', 'P&RS'), ('SPM', 'SPM'), ('AES', 'AES')], validators=[DataRequired()])
    submit = SubmitField('Next')

# Application Page Form (Chatbot)
class ApplicationForm(FlaskForm):
    prompt = StringField('Ask your question:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Redirect to login page
@app.route('/')
def home():
    return redirect(url_for('login'))  

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Use hashed passwords in production!
            login_user(user)
            return redirect(url_for('sbu'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/sbu', methods=['GET', 'POST'])
@login_required
def sbu():
    if request.method == 'POST':
        selected_sbu = request.form.get('sbu')
        if selected_sbu == 'SBU1':
            return redirect(url_for('project', sbu='SBU1'))
        elif selected_sbu == 'SBU2':
            return redirect(url_for('project', sbu='SBU2'))
    return render_template('sbu.html')

@app.route('/project', methods=['GET', 'POST'])
@login_required
def project():
    if request.method == 'POST':
        selected_project = request.form.get('project')
        return redirect(url_for('portfolio', project=selected_project))
    return render_template('project.html')

@app.route('/portfolio', methods=['GET', 'POST'])
@login_required
def portfolio():
    if request.method == 'POST':
        selected_portfolio = request.form.get('portfolio')
        return redirect(url_for('application', portfolio=selected_portfolio))
    return render_template('portfolio.html')

@app.route('/application', methods=['GET', 'POST'])
@login_required
def application():
    prompt_response = None
    if request.method == 'POST':
        user_prompt = request.form.get('prompt')
        prompt_response = get_chatbot_response(user_prompt)  # Call the chatbot response function
    return render_template('application.html', prompt_response=prompt_response)

def get_chatbot_response(user_input):
    # Simple rule-based responses for demonstration purposes
    responses = {
        "hello": "Hello! How can I assist you today?",
        "what is your name?": "I am a simple chatbot created to help you.",
        "how can I help you?": "You can ask me about our services or projects.",
        "bye": "Goodbye! Have a great day!",
    }
    
    # Return response if found, else return a default message
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()  # Create database tables if they don't exist.
    app.run(debug=True)