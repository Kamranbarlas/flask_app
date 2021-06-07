from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e6b1bb2211fe6a1f17af62811f296f7b'

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


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)