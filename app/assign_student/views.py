from flask import *

from app.assign_student import assign_student_bp
from app.assign_student.forms import assign_studentform
@assign_student_bp.route("/assign_student_list")

def get_assign_student_list():
    return render_template("list_assign_student.html")


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@assign_student_bp.route('/add_assign_student', methods=['GET', 'POST'])
def add_assign_student():
    form=assign_studentform()
    if form.validate_on_submit():
        assign_student_name=form.assign_student_name.data
        assign_student_code=form.assign_student_code.data
        #insert the record
        return redirect(url_for('assign_student.get_assign_student_list'))
    return render_template('add_assign_student.html', form=form)

    