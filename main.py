from flask import Flask, render_template,url_for,flash,redirect
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
        flash('Login UnSuccessfull. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)