from flask import *
from app.department import department_bp
from app.department.forms import DepartmentForm
from app.department.models import Department
from app import db

# Route to display the department list
@department_bp.route("/department_list", methods=['GET'])
def get_department_list():
    department = Department.query.all()
    return render_template("list_department.html", dp=Department)

# Route to add a new department
@department_bp.route('/add_department', methods=['GET', 'POST'])
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        name = form.department_name.data
        code = form.department_code.data
        # Insert the record
        new_department = Department(name=name, code=code)
        db.session.add(new_department)
        db.session.commit()
        return redirect(url_for('department.get_department_list'))
    return render_template('add_department.html', form=form)

# Route to delete a department by ID
@department_bp.route('/delete_department/<int:id>', methods=['POST'])
def delete_department(id):
    departments = Department.query.get_or_404(id)
    db.session.delete(Department)
    db.session.commit()
    return redirect(url_for('department.get_department_list'))
    
#method to update department record
@department_bp.route('/edit_department/<int:id>', methods=['GET', 'POST'])
def update_department(id):
    Department=Department.query.get_or_404(id)
    form=DepartmentForm(obj=Department)
    if form.validate_on_submit():
        form.populate_obj (Department)
        db.session.commit()
        return redirect(url_for('department.get_department_list'))
    return render_template('add_department.html', form=form)

#method to delete all department table
@department_bp.route('/delete_all_department/', methods=['POST'])
def delete_all_department():
    Department.query.delete()
    db.session.commit()
    return "All department records deleted", 200