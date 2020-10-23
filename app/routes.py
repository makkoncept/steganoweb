import os
import uuid

from PIL import Image
from flask import render_template, redirect, url_for

from app import app
from app.forms import SecretMessageEncodeForm, SecretMessageDecodeForm
from app.helper import encode_message, decode_message


@app.route("/", methods=["GET", "POST"])
def index():
    form = SecretMessageEncodeForm()
    if form.validate_on_submit():  # if server side validation passes
        message = form.message.data
        processed_filename = encode_message(form.photo.data, message)

        return redirect(url_for("picture", image_name=processed_filename))

    return render_template("index.html", form=form)


@app.route("/picture/<image_name>")
def picture(image_name):
    src = url_for("static", filename="images/" + image_name)
    return render_template("picture.html", src=src)


@app.route("/decode", methods=["GET", "POST"])
def decode():
    form = SecretMessageDecodeForm()
    if form.validate_on_submit():
        message = decode_message(form.photo.data)
        if message is None:
            message = "no_hidden_message"
        return render_template("decode.html", form=form, hidden_message=message)
    return render_template("decode.html", form=form, hidden_message=None)
