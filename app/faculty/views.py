from flask import *

from app.faculty import faculty_bp
from app.faculty.forms import Facultyform
from app.faculty.models import Faculty
from app import db
@faculty_bp.route("/faculty_list", methods=['GET'])

def get_faculty_list():
    faculty=Faculty.query.all()
    return render_template("list_faculty.html",fac=faculty)


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@faculty_bp.route('/add_faculty', methods=['GET', 'POST'])
def add_faculty():
    form=Facultyform()
    if form.validate_on_submit():
        faculty_name=form.faculty_name.data
        faculty_code=form.faculty_code.data
        #insert the record
        new_faculty=Faculty(name=faculty_name,code= faculty_code)
        db.session.add( new_faculty)
        db.session.commit()
        return redirect(url_for('faculty.get_faculty_list'))
    return render_template('add_faculty.html', form=form)

    