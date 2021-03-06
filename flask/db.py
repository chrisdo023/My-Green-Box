import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DATABASE = "cabinet.db"

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Creating function to run SQL commands in schema.sql
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

        print('\n\nInitialized the database.\n\n')