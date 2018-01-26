from flask import render_template, url_for, Blueprint

from flare.db import db

view = Blueprint('view', __name__, template_folder='templates')


@view.route('/')
def get_index():
    return render_template('index.html')


@view.route('/<string:fire_name>')
def get_fire(fire_name):
    dbc = db.get()
    dbc.execute('SELECT * FROM fire WHERE name = %s' % fire_name)

    return render_template('fire.html', fire_name=fire_name)


@view.route('/<string:fire_name>/<int:flame_id>')
def get_flame(fire_name, flame_id):
    return fire_name + str(flame_id)


@view.route('/<string:fire_name>/<int:flame_id>/kindle')
def kindle_flame(fire_name, flame_id):
    print(fire_name + str(flame_id))

    return url_for('get_flame')
