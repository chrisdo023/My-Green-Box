import datetime
import sqlite3

from flask import Flask, render_template, g, request

from ___future___ import print_function
import sys

app = Flask(__name__)

# default cabinet.db
DATABASE = 'cabinet.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    else:
        print("Unsuccessfully connected to SQLite")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.before_first_request
def create_app():
    app = ...
    from . import db
    db.init_db(app)

    return app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method == 'POST':
        try:
            id = request.form["Id"]
            temperature = request.form["Temperature"]
            humidity = request.form["Humidity"]
            createdAt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            with sqlite3.connect("cabinet.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO cabinet(id, temperature, humidity, created_at) VALUES (?,?,?,?)", (ident, temperature, humidity, createdAt))

                con.commit()
                msg = "Temperature and humidity successfully added"
        except:
            con.rollback()
            msg = "cannot connect to db"
            return render_template("result.html", msg = msg)
        finally:
            return render_template("result.html", msg = msg)
            con.close()    

@app.route('/list')
def list():
    con = sqlite3.connect('cabinet.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from cabinet")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)

if __name__ == "__main__":
    app.run(debug= True)