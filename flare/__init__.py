from flask import Flask

from flare.db.db import db
from flare.views.views import view

app = Flask(__name__)
app.config.from_object('config.Dev')
app.register_blueprint(db)
app.register_blueprint(view)


@app.cli.command('initdb')
def initdb_command():
    init()
    print('Database initialized')


if __name__ == '__main__':
    app.run()
