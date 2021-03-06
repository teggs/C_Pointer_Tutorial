from flask_login import UserMixin
from app import db,login

@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    save_the_answer = db.Column(db.String(80))
    question_index = db.Column(db.String(80))
    flag = db.Column(db.Integer)
    emh = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username
