from app import db


class Faculty(db.Model):
    _tablename_='faculty'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False, unique=True)
    code=db.Column(db.String(10), nullable=False, unique=True)
    
    def _repr_(self):
        return f'<Faculty>{self.name}'