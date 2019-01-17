from stegano import lsb


def encode(img_path, message, save_path):
    secret = lsb.hide(img_path, message)
    secret.save(save_path)


def decode_message(img_path):
    message = lsb.reveal(img_path)
    return message
