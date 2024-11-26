from flask import *

from app.level import level_bp
from app.level.forms import levelform
@level_bp.route("/level_list")

def get_level_list():
    return render_template("list_level.html")


#Get--retrieves information and passes the information to the html page
#POST-- to submit the data
#put
#delete-- to remove/delete


@level_bp.route('/add_level', methods=['GET', 'POST'])
def add_level():
    form=levelform()
    if form.validate_on_submit():
        level_name=form.level_name.data
        level_code=form.level_code.data
        #insert the record
        return redirect(url_for('level.get_level_list'))
    return render_template('add_level.html', form=form)

    