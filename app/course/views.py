from flask import *

from app.course import course_bp
from app.course.forms import Courseform
@course_bp.route("/course_list")

def get_course_list():
    return render_template("list_course.html")


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@course_bp.route('/add_course', methods=['GET', 'POST'])
def add_course():
    form=Courseform()
    if form.validate_on_submit():
        course_name=form.course_name.data
        course_code=form.course_code.data
        #insert the record
        return redirect(url_for('course.get_course_list'))
    return render_template('add_course.html', form=form)

    