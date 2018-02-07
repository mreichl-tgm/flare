from bson.objectid import ObjectId
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo

from forms import TitleContentForm

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


@app.route("/<string:fire_name>", methods=["GET", "POST"])
def get_fire(fire_name):
    """
    Returns the contents of the given fire name

    :param fire_name: unique fire name
    :rtype: str
    :return: Rendered html page
    """
    fire = mongo.db.fire.find_one_or_404({"name": fire_name})
    flames = mongo.db.fire.find({"fire": fire_name})

    form = TitleContentForm()
    if form.validate_on_submit():
        flame = {
            "fire": fire_name,
            "title": request.args["title"],
            "content": request.args["name"],
            "fuel": 1
        }

        flame_id = mongo.db.fire.insert_one(flame)

        return redirect(url_for("get_flame", fire_name=fire_name, flame_id=))

    return render_template("fire.html",
                           fire_name=fire_name,
                           fire_title=fire["title"],
                           fire_description=fire["description"],
                           flames=flames,
                           form=form)


@app.route("/<string:fire_name>/<string:flame_id>")
def get_flame(fire_name, flame_id):
    """
    Returns the contents of the given flame in the given fire

    :param fire_name: Unique name of the flame
    :param flame_id: Unique id of the flame
    :rtype: str
    :return: Rendered html page
    """
    flame = mongo.db.fire.find_one_or_404({"_id": ObjectId(flame_id),
                                           "fire": fire_name})

    return render_template("flame.html",
                           flame_id=flame_id,
                           fire_name=fire_name,
                           flame_title=flame["title"],
                           flame_content=flame["content"],
                           flame_fuel=flame["fuel"])


@app.route("/create", methods=["POST"])
def create_fire():
    """
    Create a new fire if it does not already exist
    :return: Redirect to fire name
    """
    fire = {
        "name": request.args["name"],
        "title": request.args["title"],
        "description": request.args["description"],
        "flames": []
    }

    if not mongo.db.fire.find_one("name"):
        mongo.db.fire.insert_one(fire)

    return redirect(url_for("get_fire", fire_name=fire["name"]))


@app.route("/<string:fire_name>/<string:flame_id>", methods=["POST"])
def kindle_flame(fire_name, flame_id):
    """
    Add fuel to a flame

    :param fire_name: Unique id of a fire
    :param flame_id: Unique id of a flame
    :return: Redirects the user to the get_flame page
    """
    # Increase the fuel by one
    mongo.db.fire.update_one({"_id": ObjectId(flame_id),
                              "fire": fire_name},
                             {"$inc": {"fuel": 1}})
    # Redirect to the original page
    return redirect(url_for("get_flame", fire_name=fire_name, flame_id=flame_id))


if __name__ == '__main__':
    app.run()
