from flask import Flask, render_template, url_for, redirect
from flask_pymongo import PyMongo

# Create the flask application
app = Flask(__name__)
app.config.from_object("config.Dev")
# Add mongodb
mongo = PyMongo(app)


@app.route("/")
def get_index():
    """
    Returns the index page of the application website

    :rtype: str
    :return: Rendered html page
    """
    return render_template("index.html")


@app.route("/<string:fire_name>")
def get_fire(fire_name):
    """
    Returns the contents of the given fire name

    :param fire_name: unique fire name
    :rtype: str
    :return: Rendered html page
    """
    cursor = mongo.db.fire.find_one_or_404({"name": fire_name})

    return render_template("fire.html",
                           fire_title=cursor["title"],
                           fire_description=cursor["description"])


@app.route("/<string:fire_name>/<int:flame_id>")
def get_flame(fire_name, flame_id):
    """
    Returns the contents of the given flame in the given fire

    :param fire_name: Unique name of the flame
    :param flame_id: Unique id of the flame
    :rtype: str
    :return: Rendered html page
    """
    cursor = mongo.db.fire.find_one_or_404({"id": flame_id, "fire": fire_name})

    return render_template("flame.html",
                           flame_id=flame_id,
                           fire_name=fire_name,
                           flame_title=cursor["title"],
                           flame_content=cursor["content"],
                           flame_fuel=cursor["fuel"])


@app.route("/<string:fire_name>/<int:flame_id>", methods=['POST'])
def kindle_flame(fire_name, flame_id):
    """
    Add fuel to a flame

    :param fire_name: Unique id of a fire
    :param flame_id: Unique id of a flame
    :return: Redirects the user to the get_flame page
    """
    # Increase the fuel by one
    mongo.db.fire.update_one({"id": flame_id, "fire": fire_name}, {"$inc": {"fuel": 1}})
    # Redirect to the original page
    return redirect(url_for("get_flame", fire_name=fire_name, flame_id=flame_id))


if __name__ == '__main__':
    app.run()
