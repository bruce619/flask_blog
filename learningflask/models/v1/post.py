from datetime import datetime
from learningflask import db


class Post(db.Model):
    __tablename__ = 'post'  # table name will default to name of the model

    # create db columns in table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"