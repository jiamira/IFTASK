from flask import *

from app.program import program_bp
from app.program.forms import programform
@program_bp.route("/program_list")

def get_program_list():
    return render_template("list_program.html")


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@program_bp.route('/add_program', methods=['GET', 'POST'])
def add_program():
    form=programform()
    if form.validate_on_submit():
        program_name=form.program_name.data
        program_code=form.program_code.data
        #insert the record
        return redirect(url_for('program.get_program_list'))
    return render_template('add_program.html', form=form)

    