from flask import Flask, app, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from password import get_password

db=SQLAlchemy()
migrate=Migrate()

DB_USER='root'
DB_PASSWORD= 'amiriri'
DB_HOST='localhost'
DB_NAME='student_course_group'

def create_app():
    app = Flask(__name__)

db.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")

DATABASE_URI=f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'


app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)
migrate.init_app(app,db)

#import model
from app.faculty.models import Faculty
from app.department.models import Department

#registering the blueprints for the modules
from app.faculty import faculty_bp

    app.register_blueprint(faculty_bp)

    from app.department import department_bp

    app.register_blueprint(department_bp)

    from app.group import group_bp

    app.register_blueprint(group_bp)

    from app.level import level_bp

    app.register_blueprint(level_bp)

    from app.program import program_bp

    app.register_blueprint(program_bp)

    
    from app.course import course_bp

    app.register_blueprint(course_bp)

    from app.student import student_bp

    app.register_blueprint(student_bp)

    from app.assign_student import assign_student_bp

    app.register_blueprint(assign_student_bp)



    with app.app_context():
    db.create_all()

    return app