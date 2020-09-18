import os


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY") or "ujxnPZCAnfoAglcte8AsPDRZCZkmDOtde2TD2sL4"
    )
