from flask_wtf import *
from wtforms import *
from wtforms.validators import *
from app.department.models import Department

class Departmentform(FlaskForm):
    id=HiddenField('id')
<<<<<<< HEAD
    department_id=SelectField('Select department')
=======
    #faculty_id=SelectField('Select Faculty')
>>>>>>> 334f2ed3c93b64ba9ebcb34ae355448ad7f23516
    department_name=StringField('Department Name:', validators=[DataRequired()])
    department_code=StringField('Department Code:', validators=[DataRequired()])
    submit=SubmitField('Save Changes')

<<<<<<< HEAD
def __init__(self, *args, **kwargs):
    super(departmentform, self).__init__(*args, **kwargs)
    self.department_id.choices=[(department.id, department.name)for department in Department.query.all()]
=======
# def __init__(self, *args, **kwargs):
#     super(Departmentform, self).__init__(*args, **kwargs)
#     self.faculty_id.choices=[(Faculty.id, Faculty.name)for faculty in Faculty.query.all()]
>>>>>>> 334f2ed3c93b64ba9ebcb34ae355448ad7f23516
