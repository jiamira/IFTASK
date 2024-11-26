from app import db

class Program(db.Model):
    _tablename_= 'program'
    id = db.Column(db.Integer, primary_key = True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable = False)
    name = db.Column(db.String(50), nullable = False, unique = True)
    code = db.Column(db.String(10), nullable = False, unique = True)


    def _repr_(self):
        return f'<Program>{self.name}'