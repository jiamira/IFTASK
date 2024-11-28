from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.department.models import Department

class ProgramForm(FlaskForm):
    id = HiddenField("id")
    department_id=SelectField("Select dEPARTMENT")
    name=StringField("Program Name: ", validators=[data_required()])
    code=StringField("Program Code: ", validators=[data_required()])
    submit=SubmitField("Save Changes")

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        self.department_id.choices=[(department.id, department.name) for department in Department.query.all()]

    