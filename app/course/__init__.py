from flask import Blueprint


course_bp=Blueprint('course',__name__, template_folder="templates", static_folder= 'statics')

from app.course import views