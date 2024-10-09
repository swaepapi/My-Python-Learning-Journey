from app import db
    

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}  # This allows extending the existing table

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"User('{self.email}')"
