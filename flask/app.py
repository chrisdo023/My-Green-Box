import sqlite3, datetime, os.path
from flask import Flask, render_template, g, request, jsonify

app = Flask(__name__)

# default cabinet.db
DATABASE = 'cabinets.db'
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
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # db_path = os.path.join(BASE_DIR, "cabinet.db")
    # con = sqlite3.connect(db_path)
    # cur = con.cursor()

    # data = cur.execute("SELECT * FROM cabinet").fetchall()[-1]
    # temperature = data[1]
    # humidity = data[2]

    # date = str(datetime.date.today().day) + " " + str(MONTH[datetime.date.today().month - 1])
    
    # # Index page should read in database for any Cabinets available

    # return render_template('index.html', date=date, temperature=temperature, humidity=humidity)
    con = get_db()
    cur = con.cursor()

    # List tables
    listcmd = "SELECT name FROM sqlite_master WHERE type='table' AND name <> 'sqlite_sequence'"
    items = cur.execute(str(listcmd))
    items = items.fetchall()

    cabinets = []
    for item in items:

        # Fetch content from tables
        fetchcmd = ("SELECT * FROM table").replace("table", item[0], 1)
        results = cur.execute(str(fetchcmd))
        results = (results.fetchall())[0]

        dict = {
            'cabinet': item[0],
            'temp': results[1],
            'humid': results[2],
            'createdAt': results[3]
        }

        cabinets.append(dict)

    # Commit the changes to DB & close the connection
    con.commit()
    con.close()

    return render_template('index.html', cabinets=cabinets)


# POST: Update DB with Temperature and Humidity
@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method == 'POST':
        con = get_db()
        cur = con.cursor()

        # cabinet = request.form["Cabinet"]
        # print("Cabinet: ", cabinet)
        # # temperature = request.form["Temperature"]
        # # humidity = request.form["Humidity"]
        # # createdAt = request.form["CreatedAt"]
        # temperature = 78.0
        # humidity = 79.7
        # createdAt = '2022-06-19 23:20:00'
        qtc_data = request.get_json()

        results = {'processed': 'true'}

        countcmd = ("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='table'").replace('table', qtc_data[0]['cabinet'], 2)
        countcmd = countcmd.replace(qtc_data[0]['cabinet'], "table", 1)
        num = cur.execute(str(countcmd))
        if num.fetchone()[0] == 0:
            createcmd = ("CREATE TABLE table (id INTEGER PRIMARY KEY AUTOINCREMENT, temperature REAL(3) NOT NULL, humidity REAL(3) NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)").replace('table', qtc_data[0]['cabinet'], 1)
            cur.execute(str(createcmd))

        insertcmd = ("INSERT INTO table (id, temperature, humidity, created_at) VALUES (?, ?, ?, ?)").replace('table', qtc_data[0]['cabinet'], 1)
        cur.execute(str(insertcmd), (None, qtc_data[1]['temperature'], qtc_data[2]['humidity'], qtc_data[3]['createdAt']))

        # List tables
        listcmd = "SELECT name FROM sqlite_master WHERE type='table' AND name <> 'sqlite_sequence'"
        items = cur.execute(str(listcmd))
        items = items.fetchall()

        # # Fetch content from tables
        # fetchcmd = ("SELECT * FROM table").replace("table", "Rudsta", 1)
        # items = cur.execute(str(fetchcmd))
        # items = items.fetchall()

        # Commit the changes to DB & close the connection
        con.commit()
        con.close()

    # Probably will need to create some sort of dictionary from DB or SQLite makes it?
    return jsonify(results)

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

@app.route('/delete', methods = ['DELETE'])
def delete():
    if request.method == 'DELETE':
        con = get_db()
        cur = con.cursor()

        # cabinet = request.form["Cabinet"]
        # print("Cabinet: ", cabinet)
        # # temperature = request.form["Temperature"]
        # # humidity = request.form["Humidity"]
        # # createdAt = request.form["CreatedAt"]
        # temperature = 78.0
        # humidity = 79.7
        # createdAt = '2022-06-19 23:20:00'
        qtc_data = request.get_json()

        results = {'deleted': 'true'}

        deletecmd = ("DROP Table table").replace('table', qtc_data[0]['cabinet'], 1)
        cur.execute(str(deletecmd))

        # Commit the changes to DB & close the connection
        con.commit()
        con.close()

    return jsonify(results)
    
if __name__ == "__main__":
    app.run(debug= True, host= '0.0.0.0')