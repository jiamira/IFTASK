from flask import Blueprint


level_bp=Blueprint('level',__name__, template_folder="templates", static_folder= 'statics')

from app.level import views