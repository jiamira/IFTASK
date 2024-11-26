from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class programform(FlaskForm):
    id=HiddenField('id')
    program_name=StringField('program Name:', validators=[DataRequired()])
    program_code=StringField('program Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')