import os
import uuid

from app import app
from app.forms import SecretMessageEncodeForm, SecretMessageDecodeForm
from app.helper import encode, decode_message
from flask import render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename
from PIL import Image


@app.route("/", methods=["GET", "POST"])
def index():
    form = SecretMessageEncodeForm()
    if form.validate_on_submit():
        if form.photo.data:
            f = form.photo.data
            filename = secure_filename(f.filename)
            _, ext = os.path.splitext(filename)
            filename = uuid.uuid4().hex + ext
            path = os.path.join(app.root_path, "static/images", filename)
            f.save(path)
            save_file_name = "hid" + filename
            save_path = os.path.join(app.root_path, "static/images", save_file_name)
        else:
            path = os.path.join(app.root_path, "static/images", "default.png")
            save_file_name = uuid.uuid4().hex + ".png"
            save_path = os.path.join(app.root_path, "static/images", save_file_name)
        message = form.message.data
        f = Image.open(path)
        encode(path, message, save_path)

        return redirect(
            url_for("picture", name=save_file_name, height=f.height, width=f.width)
        )

    return render_template("index.html", form=form)


@app.route("/picture/<name>/<height>/<width>")
def picture(name, height, width):
    src = url_for("static", filename="images/" + name)
    height, width = img_tag_size(int(height), int(width))
    return render_template("picture.html", src=src, height=height, width=width)


def img_tag_size(height, width):
    if height < 850 and width < 850:
        return height, width
    else:
        while height > 850 and width > 850:
            height = int(height / 2)
            width = int(width / 2)
        return height, width


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

