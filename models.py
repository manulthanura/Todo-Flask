from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    # complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.title} created on {self.date}'