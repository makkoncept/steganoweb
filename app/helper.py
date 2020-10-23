import os
import uuid

from stegano import lsb
from werkzeug.utils import secure_filename

from app import app


def encode_message(image, message):
    image_with_secret = lsb.hide(image, message)
    filename = f"{uuid.uuid4().hex}.png"  # giving a random name to the file
    image_path = os.path.join(
        app.root_path, "static/images", filename
    )  # to work with stegano, the image will be saved as a png
    image_with_secret.save(image_path)  # save the processed image
    return filename


def decode_message(image):
    message = lsb.reveal(image)
    return message
