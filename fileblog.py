#having imported flask and using a virtual environment, my code still does not run even for a code as simple as

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello jupiter"

# set FLASK_APP=projectname  doesnt work, same with other online solutions
