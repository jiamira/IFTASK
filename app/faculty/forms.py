from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import *

class FacultyForm(FlaskForm):
    id = HiddenField("id")
    name=StringField("Faculty Name: ", validators=[DataRequired()])
    code=StringField("Faculty Code: ", validators=[DataRequired()])
    submit=SubmitField("Save Changes")

    