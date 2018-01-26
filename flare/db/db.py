import sqlite3

from flask import g, Blueprint

db = Blueprint('db', __name__)


def connect():
    conn = sqlite3.connect('flare.db')
    conn.row_factory = sqlite3.Row

    return conn


def get():
    if not hasattr(g, 'db'):
        g.db = connect()
    return g.db


@db.teardown_request
def close():
    if hasattr(g, 'db'):
        g.db.close()


def init():
    conn = get()
    with db.open_resource('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
