from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class assign_studentform(FlaskForm):
    id=HiddenField('id')
    assign_student_name=StringField('assign_student Name:', validators=[DataRequired()])
    assign_student_code=StringField('assign_student Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')