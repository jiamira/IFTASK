from flask import *

from app.department import department_bp
from app.department.models import Department
from app.department.forms import departmentform
from app import db 
@department_bp.route("/department_list")

def get_department_list():
    return render_template("list_department.html")


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@department_bp.route('/add_department', methods=['GET', 'POST'])
def add_department():
    form=departmentform()
    if form.validate_on_submit():
        faculty_id=form.faculty_id.data 
        department_name=form.department_name.data
        department_code=form.department_code.data
        #insert the record to the relational database management system
        new_department=Department(faculty_id=faculty_id,name=department_name,code= department_code)
        db.session.add( new_department)
        db.session.commit()
        return redirect(url_for('department.get_department_list'))
    return render_template('add_department.html', fm=form)

    