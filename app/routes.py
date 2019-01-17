from app import app
from app.forms import SecretMessageForm
from flask import render_template


@app.route("/", methods=["GET", "POST"])
def home():
    form = SecretMessageForm()
    if form.validate_on_submit:
        return "yes"
    return render_template("index.html", form=form)


@app.route("/decode")
def decode():
    form = SecretMessageForm()
    return render_template("index.html", form=form)
