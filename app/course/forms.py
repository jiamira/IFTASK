from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class Courseform(FlaskForm):
    id=HiddenField('id')
    course_name=StringField('course Name:', validators=[DataRequired()])
    course_code=StringField('course Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')