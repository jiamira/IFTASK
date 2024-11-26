from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class Facultyform(FlaskForm):
    id=HiddenField('id')
    faculty_name=StringField('Faculty Name:', validators=[DataRequired()])
    faculty_code=StringField('Faculty Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')