import sqlite3
from flask import Flask, request, g, jsonify, make_response
from markupsafe import escape
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def create_db():
    c = get_db()
    c.execute("CREATE TABLE IF NOT EXISTS usuarios (\
                id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, senha TEXT\
            )")

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

@app.route('/')
def index():
    create_db()
    # cur = get_db().cursor()
    insert_db("INSERT INTO usuarios (email, senha) VALUES (?, ?)", ("jonas@gmail.com", "123"))
    return 'Initiate database'

@app.route('/users', methods=['GET'])
def users():
    create_db()
    users = select_db("SELECT * FROM usuarios")
    json_users = []
    for i in users:
        json_users.append({'id': i[0], 'email': i[1], 'senha': i[2]})
    print(json_users)
    return make_response(jsonify(json_users), 200)

@app.route('/user', methods=['POST'])
def user():
    create_db()
    body = request.json
    email = body.get('email')
    senha = body.get('senha')
    if body and email and senha:
        try:
            insert_db("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
            return 'User created sucessfully'
        except Exception as e:
            print(e)
            return make_response("Error", 500)

@app.route('/user', methods=['GET'])
def user_specific():
    create_db()
    body = request.json
    email = body.get('email')
    senha = body.get('senha')
    if body and email and senha:
        try:
            user_logged = select_db("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
            json_users = []
            for i in user_logged:
                json_users.append({'id': i[0], 'email': i[1], 'senha': i[2]})
            return make_response(jsonify(json_users), 200)
        except Exception as e:
            print(e)
            return make_response("Error", 500)

@app.route('/user/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    create_db()
    try:
        insert_db("DELETE FROM usuarios WHERE id = ?", (id_user,))
        return 'User deleted sucessfully'
    except Exception as e:
        print(e)
        return make_response("Error", 500)
