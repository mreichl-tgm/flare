from bson import ObjectId
from flask import Flask, render_template, url_for, redirect, request
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


@app.route("/", methods=["POST"])
def add_fire():
    """
    Create a new fire if it does not already exist
    :return: Redirect to fire name
    """
    fire = {"name": request.form["name"],
            "title": request.form["title"],
            "description": request.form["description"],
            "flames": []}

    if not mongo.db.fire.find_one("name"):
        mongo.db.fire.insert_one(fire)

    return redirect(url_for("get_fire", fire_name=fire["name"]))


@app.route("/<string:fire_name>")
def get_fire(fire_name: str):
    """
    Returns the contents of the given fire name

    :param fire_name: unique fire name
    :rtype: str
    :return: Rendered html page
    """
    fire = mongo.db.fire.find_one_or_404({"name": fire_name})
    flames = mongo.db.fire.find({"fire": fire_name})

    return render_template("fire.html",
                           fire_name=fire_name,
                           fire_title=fire["title"],
                           fire_description=fire["description"],
                           flames=flames)


@app.route("/<string:fire_name>", methods=["POST"])
def add_flame(fire_name):
    flame = {"fire": fire_name,
             "title": request.form["title"],
             "content": request.form["content"],
             "fuel": 1}

    flame_id = mongo.db.fire.insert_one(flame).inserted_id

    return redirect(url_for("get_flame", fire_name=fire_name, flame_id=flame_id))


@app.route("/<string:fire_name>/<string:flame_id>")
def get_flame(fire_name: str, flame_id: str):
    """
    Returns the contents of the given flame in the given fire

    :param fire_name: Unique name of the flame
    :param flame_id: Unique id of the flame
    :rtype: str
    :return: Rendered html page
    """
    flame = mongo.db.fire.find_one_or_404({"_id": ObjectId(flame_id)})

    return render_template("flame.html",
                           flame_id=flame_id,
                           fire_name=fire_name,
                           flame_title=flame["title"],
                           flame_content=flame["content"],
                           flame_fuel=flame["fuel"])


@app.route("/<string:fire_name>/<string:flame_id>", methods=["POST"])
def kindle(fire_name: str, flame_id: str):
    """
    Add fuel to a flame

    :param fire_name: Unique id of a fire
    :param flame_id: Unique id of a flame
    :return: Redirects the user to the get_flame page
    """
    # Increase the fuel by one
    mongo.db.fire.update_one({"_id": ObjectId(flame_id)}, {"$inc": {"fuel": 1}})
    # Redirect to original page
    return redirect(request.path)


if __name__ == '__main__':
    app.run()
