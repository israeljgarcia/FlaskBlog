from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Miguel' }
    posts = [
        {
            'author': { 'username' : 'John' },
            'body': 'Beautiful day in Portland!'
        },

        {
            'author': { 'username': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        },

        {
            'author': { 'username': 'Chicken' },
            'body': 'This is my original post and I like it!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
