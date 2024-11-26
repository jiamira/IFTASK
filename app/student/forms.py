from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class studentform(FlaskForm):
    id=HiddenField('id')
    student_name=StringField('student Name:', validators=[DataRequired()])
    student_code=StringField('student Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')