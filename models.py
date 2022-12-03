from flask_sqlalchemy import SQLAlchemy
from app import app


app.config['SECRET_KEY'] =  '123'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'
db = SQLAlchemy(app)


class InsertData(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    email = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(50),nullable=False)
def __repr__(self):
    return self.name
