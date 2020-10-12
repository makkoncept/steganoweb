import os
import uuid

from PIL import Image
from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for, request, session

from app import app, DEFAULT_FILE_PATH
from app.forms import SecretMessageEncodeForm, SecretMessageDecodeForm
from app.helper import encode_message, decode_message


@app.route("/", methods=["GET", "POST"])
def index():
    form = SecretMessageEncodeForm()
    if form.validate_on_submit():  # if server side validation passes
        message = form.message.data
        if form.photo.data:  # if the user has provided their own image
            processed_filename = encode_message(form.photo.data, message)
        else:
            default_image = Image.open(DEFAULT_FILE_PATH)
            processed_filename = encode_message(default_image, message)

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
        f = form.photo.data
        filename = secure_filename(f.filename)
        _, ext = os.path.splitext(filename)
        filename = uuid.uuid4().hex + ext
        path = os.path.join(app.root_path, "static/images", filename)
        f.save(path)
        message = decode_message(path)
        if message is None:
            message = "no_hidden_message"
        return render_template("decode.html", form=form, hidden_message=message)
    return render_template("decode.html", form=form, hidden_message=None)

