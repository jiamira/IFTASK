from flask import Blueprint


group_bp=Blueprint('group',__name__, template_folder="templates", static_folder= 'statics')

from app.group import views