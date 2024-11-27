from flask import *
from app.faculty import faculty_bp
from app.faculty.forms import Facultyform 
from app.faculty.models import Faculty
from app import db

@faculty_bp.route('/faculty_list', methods=['GET'])
def get_faculty_list():
    faculty=Faculty.query.all()
    return render_template ('list_faculty.html', fac=faculty)

#GET--retrieve information and then pass the information to the html page
#POST -- to submit the data
#PUT
#DELETE --delete or to remove

@faculty_bp.route('/add_faculty', methods=['GET', 'POST'])
def add_faculty():
    forms=Facultyform()
    if forms.validate_on_submit():
        name=forms.name.data
        code=forms.code.data
        #insert the record
        new_faculty=Faculty(name=name, code=code)
        db.session.add(new_faculty)
        db.session.commit()
        return redirect(url_for('faculty.get_faculty_list'))
    return render_template('add_faculty.html', form=forms)

#method to delete a row from a faculty table
@faculty_bp.route('/delete_faculty/<int:id>', methods=['POST'])
def delete_faculty(id):
    faculty=Faculty.query.get_or_404(id)
    db.session.delete(faculty)
    db.session.commit()
    return redirect(url_for('faculty.get_faculty_list'))


#method to update faculty record
@faculty_bp.route('/edit_faculty/<int:id>', methods=['GET', 'POST'])
def update_faculty(id):
    faculty=Faculty.query.get_or_404(id)
    form=Facultyform(obj=faculty)
    if form.validate_on_submit():
        form.populate_obj(faculty)
        db.session.commit()
        return redirect(url_for('faculty.get_faculty_list'))
    return render_template('add_faculty.html', form=form)


#method to delete all faculty table
@faculty_bp.route('/delete_all_faculty/', methods=['POST'])
def delete_all_faculty():
    Faculty.query.delete()
    db.session.commit()
    return redirect(url_for('faculty.get_faculty_list'))