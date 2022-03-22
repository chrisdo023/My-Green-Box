import sqlite3

from flask import Flask, render_template, g

app = Flask(__name__)

# default cabinet.db
DATABASE = 'cabinet.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.before_first_request
def create_app():
    print('\ndb.init_app\n')
    # import db
    # db.init_app(app)

    # return app

    cur = get_db().cursor()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug= True)