from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class groupform(FlaskForm):
    id=HiddenField('id')
    group_name=StringField('group Name:', validators=[DataRequired()])
    group_code=StringField('group Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')