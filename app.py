import sqlite3

from flask import Flask, render_template, url_for, g

app = Flask(__name__)
app.config.from_object('config.Dev')


@app.route('/')
def get_index():
    return render_template('index.html')


@app.route('/<string:fire_name>')
def get_fire(fire_name):
    return render_template('fire.html', fire_name=fire_name)


@app.route('/<string:fire_name>/flame/<int:flame_id>')
def get_flame(fire_name, flame_id):
    return fire_name + str(flame_id)


@app.route('/<string:fire_name>/flame/<int:flame_id>/kindle')
def kindle_flame(fire_name, flame_id):
    print(fire_name + str(flame_id))

    return url_for('get_flame')


def connect_db():
    dbc = sqlite3.connect(app.config['DATABASE'])
    dbc.row_factory = sqlite3.Row

    return dbc


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Database initialized')


if __name__ == '__main__':
    app.run()
