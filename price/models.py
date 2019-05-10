from app import db

class Price(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    
    username = db.Column(db.String(80), unique=True)
    

    def __repr__(self):
        return '<Price %r>' % self.id

    def to_dict(self):
        return dict(
            
        )