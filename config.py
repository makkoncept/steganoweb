import os


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "ujxnPZCAnfoAglcte8AsPDRZCZkmDOtde2TD2sL4"
    )
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024