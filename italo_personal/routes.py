from flask import render_template
from italo_personal import app

@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template('main.html')

