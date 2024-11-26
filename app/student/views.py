from flask import *

from app.student import student_bp
from app.student.forms import studentform
@student_bp.route("/student_list")

def get_student_list():
    return render_template("list_student.html")


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@student_bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form=studentform()
    if form.validate_on_submit():
        student_name=form.student_name.data
        student_code=form.student_code.data
        #insert the record
        return redirect(url_for('student.get_student_list'))
    return render_template('add_student.html', form=form)

    