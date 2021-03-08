import sqlite3
from flask import Flask, request, g, jsonify, make_response
from markupsafe import escape
app = Flask(__name__)

@app.errorhandler(500)
def not_found(error):
    return make_response("Error", 500)
    # return 'Error 500 - Internal Server Error'

@app.errorhandler(404)
def not_found(error):
    return make_response("Error", 404)
    # return 'Error 404 - Not Found'

@app.errorhandler(400)
def not_found(error):
    return make_response("Error", 400)
    # return 'Error 400 - Bad Request'

@app.route('/')
def index():
    cur = get_db().cursor()
    return 'Initiate database'

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def create_db():
    c = get_db()
    c.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT)")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def select_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_db(query, args=()):
    con = get_db()
    con.execute(query, args)
    con.commit()

@app.route('/users')
def users():
    create_db()
    users = select_db("SELECT * FROM usuarios")
    json_users = []
    for i in users:
        json_users.append({'name': i[0]})
    print(json_users)
    return jsonify(json_users)

@app.route('/user', methods=['GET', 'POST'])
def user():
    create_db()
    if request.method == 'POST':
        print("POST METHOD")
        body = request.json
        name = body.get('name')
        if body and name:
            try:
                insert_db("INSERT INTO usuarios VALUES (?)", (name,))
                return 'User created sucessfully'
            except:
                return 'Error at creating User'
    else:
        print("GET METHOD")