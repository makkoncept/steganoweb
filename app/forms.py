from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField, StringField, BooleanField
from wtforms.validators import NumberRange, Length, DataRequired, ValidationError


class SecretMessageEncodeForm(FlaskForm):
    # photo = FileField("Upload Image", validators=[FileRequired(), FileAllowed(["png"])])
    photo = FileField("Upload Image", validators=[FileAllowed(["png"])])
    message = StringField("Secret message", validators=[DataRequired(), Length(1, 100)])


class SecretMessageDecodeForm(FlaskForm):
    photo = FileField("Upload Image", validators=[DataRequired(), FileAllowed(["png"])])

