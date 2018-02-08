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
