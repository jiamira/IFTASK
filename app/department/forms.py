from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.faculty.models import Faculty

class DepartmentForm(FlaskForm):
    id = HiddenField("id")
    faculty_id=SelectField("Select Faculty")
    department_name=StringField("Department Name: ", validators=[data_required()])
    department_code=StringField("Department Code: ", validators=[data_required()])
    submit=SubmitField("Save Changes")

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.faculty_id.choices=[(faculty.id, faculty.name) for faculty in Faculty.query.all()]

    