from flask import Flask, url_for, request, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "DO THE LOGIN"
    else:
        return "LOGIN FORM USER"

@app.route('/hi')
def hi(name=None):
    return render_template('hello.html', name=name)
@app.route('/hi/<name>')
def hi_name(name=None):
    return render_template('hello.html', name=name)

# STORING FILE AT /STATIC WILL RETURN A STATIC FILE AS STYLE.CSS
#url_for('static', filename='style.css')

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))