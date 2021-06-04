from flask import Flask, render_template, url_for
app = Flask(__name__)


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
