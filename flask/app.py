import sqlite3, datetime, os.path
from flask import Flask, render_template, g, request

app = Flask(__name__)

# default cabinet.db
DATABASE = 'cabinet.db'
database = 'cabinet'
MONTH = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, DATABASE)
        db = g._database = sqlite3.connect(db_path)
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
    # import db
    # db.init_db()

    # get_db()

    return app

@app.route('/')
def index():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "cabinet.db")
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    data = cur.execute("SELECT * FROM cabinet").fetchall()[-1]
    temperature = data[1]
    humidity = data[2]

    date = str(datetime.date.today().day) + " " + str(MONTH[datetime.date.today().month - 1])
    
    return render_template('index.html', date=date, temperature=temperature, humidity=humidity)

@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method == 'POST':
        try:
            con = get_db()
            cur = con.cursor()

            temperature = request.form["Temperature"]
            humidity = request.form["Humidity"]
            createdAt = request.form["CreatedAt"]

            cur.execute("INSERT INTO cabinet (id, temperature, humidity, created_at) VALUES (?, ?, ?, ?)", (None, temperature, humidity, createdAt))

            con.commit()
            con.close()
            con.close()

            msg = "Temperature and humidity recorded"
        except:
            msg = "Could not record temperature and humidity"
        finally:
            return { "status": msg } 

@app.route('/list', methods = ['GET'])
def list():
    if request.method == 'GET':
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "cabinet.db")
        con = sqlite3.connect("cabinet.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM cabinet")

        rows = cur.fetchall()

        return render_template("list.html", rows=rows)

@app.route('/retrieve', methods = ['GET'])
def retrieve():
    if request.method == 'GET':
        try:
            con = sqlite3.connect("cabinet.db")
            cur = con.cursor()

            data = cur.execute("SELECT * FROM cabinet").fetchall()[-1]
        except:
            data = []
        finally:
            return { "data": data }
    else:
        print("error")

if __name__ == "__main__":
    app.run(debug= True)