from flask import Flask, render_template,url_for,flash,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e6b1bb2211fe6a1f17af62811f296f7b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# Entering Dummy Data
posts = [
    {
        'author':"Kamran Barlas",
        'title':"Blog Post",
        'content':'Second post content',
        'date_posted':"4-5-2022"
    },
    {
        'author': "Kashan Baig",
        'title': "Blog Post 2",
        'content': 'Second post content 2',
        'date_posted': "2-5-2022"
    }

]


@app.route('/')
@app.route("/home")
def home():
    return render_template('/home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('/about.html', title="About_us")


@app.route("/register",methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'LOGGED SUCCESSFULLY {form.email.data}!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login UnSuccessfull. Please check username and password', 'dark')
    return render_template('login.html', title='Login', form=form)