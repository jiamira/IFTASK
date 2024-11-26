from flask import *

from app.group import group_bp
from app.group.forms import groupform
@group_bp.route("/group_list")

def get_group_list():
    return render_template("list_group.html")


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@group_bp.route('/add_group', methods=['GET', 'POST'])
def add_group():
    form=groupform()
    if form.validate_on_submit():
        group_name=form.group_name.data
        group_code=form.group_code.data
        #insert the record
        return redirect(url_for('group.get_group_list'))
    return render_template('add_group.html', form=form)

    