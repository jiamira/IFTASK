from flask import Blueprint


faculty_bp=Blueprint('faculty',__name__, template_folder="templates", static_folder= 'statics')

from app.faculty import views