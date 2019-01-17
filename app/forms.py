from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField, StringField
from wtforms.validators import NumberRange, Length, DataRequired


class SecretMessageForm(FlaskForm):
    photo = FileField("Upload Image", validators=[FileRequired(), FileAllowed(["png"])])
    message = StringField("Secret message", validators=[DataRequired(), Length(1, 100)])
    # palette_height = IntegerField('Palette Height', validators=[NumberRange(1, 10)])
    # palette_outline_width = IntegerField('Palette Outline Width', validators=[NumberRange(1, 40)])
