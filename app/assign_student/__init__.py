from flask import Blueprint

assign_student_bp=Blueprint('assign_student',__name__, template_folder="templates", static_folder= 'statics')

from app.assign_student import views