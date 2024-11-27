from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import *

class Facultyform(FlaskForm):
    id=HiddenField('id')
    faculty_name=StringField('Faculty Name:', validators=[DataRequired()])
    faculty_code=StringField('Faculty Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')