from flask import Blueprint


program_bp=Blueprint('program',__name__, template_folder="templates", static_folder= 'statics')

from app.program import views