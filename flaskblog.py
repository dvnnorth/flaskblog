from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Devin North',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 12, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 14, 2019'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about_page():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
