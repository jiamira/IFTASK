from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.faculty.models import Faculty

class departmentform(FlaskForm):
    id=HiddenField('id')
    faculty_id=SelectField('Select Faculty')
    department_name=StringField('Department Name:', validators=[DataRequired()])
    department_code=StringField('Department Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')

def __init__(self, *args, **kwargs):
    super(departmentform, self).__init__(*args, **kwargs)
    self.faculty_id.choices=[(Faculty.id, Faculty.name)for faculty in Faculty.query.all()]