from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo

# Create the flask application
app = Flask(__name__)
app.config.from_object("config.Dev")
# Add mongodb
mongo = PyMongo(app)


@app.route("/")
def get_index():
    return render_template("index.html")


@app.route("/<string:fire_name>")
def get_fire(fire_name):
    cursor = mongo.db.fire.find_one_or_404({"name": fire_name})

    return render_template("fire.html",
                           fire_title=cursor["title"],
                           fire_description=cursor["description"])


@app.route("/<string:fire_name>/<int:flame_id>")
def get_flame(fire_name, flame_id):
    cursor = mongo.db.fire.find_one_or_404({"_id": flame_id, "_fire": fire_name})

    return render_template("flame.html",
                           fire_name=fire_name,
                           flame_title=cursor["title"],
                           flame_content=cursor["content"])


@app.route('/<string:fire_name>/<int:flame_id>/kindle')
def kindle_flame(fire_name, flame_id):
    print(fire_name + str(flame_id))

    return url_for('get_flame')


if __name__ == '__main__':
    app.run()
