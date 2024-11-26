from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class levelform(FlaskForm):
    id=HiddenField('id')
    level_name=StringField('level Name:', validators=[DataRequired()])
    level_code=StringField('level Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')