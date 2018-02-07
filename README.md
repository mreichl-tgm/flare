Flask + ReST
============
# Vorbereitung
[Flask] [1] kann einfach über [pip] [2] installiert und über die Methode `flask run` gestartet werden.

~~~ sh
pip install flask 		# Installiere Flask
export FLASK_APP=app.py 	# Setze die Hauptklasse der Applikation
flask run 			# Starte die Applikation
~~~

## Erweitert
### Venv
Für Projekte wie dieses empfiehlt es sich zu Beginn eine isolierte Arbeitsumgebung aufzusetzen. In Python wird dazu [virtualenv] [3] verwendet.
~~~ sh
pip install virtualenv 		# Installiere Virtualenv
virtualenv venv 		# Erstelle eine neue Umgebung
source venv/bin/activate 	# Aktiviere die Umgebung
~~~
Die Umgebung sollte, sobald die Arbeit beendet ist, über das Kommando `deactivate` wieder deaktiviert werden.

### PyCharm
In PyCharm kann ein neues Flask Projekt einfach über den Reiter `File` → `New Project...` → `Flask` erstellt werden.
![Neues Projekt](img/new-light.png)

~~~
.
|-- app.py
|-- static
|-- templates
`-- venv
~~~

# Formulare
Zur Interaktion mittels Formularen wird in Flask das [Flask-WTF] [4] Paket verwendet, welches eine Schnittstelle zum [WTForms] [5]  Paket bildet.

Ein Formular wird nach seinen Eingabefeldern benannt. Unser Formular wird daher als `TitleContentForm` deklariert, da es die Eingabe eines Titels, sowie eines Textes ermöglichen soll.

```python
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class TitleContentForm(Form):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
```

Nun muss das Formular an jene Funktion übergeben werden, welche zu dessen Darstellung bestimmt ist. In unserem Fall werden in der Methode `add_flame` folgende Zeilen hinzugefügt:

~~~python
form = TitleContentForm()
if form.validate_on_submit():
	return redirect(url_for("add_flame", fire_name=fire_name))
~~~

Beim Aufruf von `render_template` wird das Formular dann über `form=form` übergeben.
~~~python
render_template("fire.html",
		# ...
		form=form)
~~~

# Author
Markus Reichl <markus@re1.at>

# Referenzen 
- [1] Flask. http://flask.pocoo.org
- [2] Python. Installing Python Modules. https://docs.python.org/3/installing/index.html
- [3] Virtualenv. Installation. https://virtualenv.pypa.io/en/stable/installation
- [4] Flask-WTF. https://flask-wtf.readthedocs.io/en/stable
- [5] WTForms. https://wtforms.readthedocs.io/en/latest

[flask]: http://flask.pocoo.org
[pip]: https://docs.python.org/3/installing/index.html
[virtualenv]: https://virtualenv.pypa.io/en/stable/installation
[flask-wtf]: https://flask-wtf.readthedocs.io/en/stable
[wtforms]: https://wtforms.readthedocs.io/en/latest
