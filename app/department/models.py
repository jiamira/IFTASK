from app import db

class Department(db.Model):
    _tablename_ = 'Department'
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('Department.id'))  # Correct table reference
    name = db.Column(db.String(50), nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)

    parent = db.relationship('Department', remote_side=[id], backref='sub_departments')  # Optional for hierarchy

    def _repr_(self):
        return f'<Department {self.name}>'