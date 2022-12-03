from flask import Flask, render_template, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField,SubmitField
from wtforms.validators import DataRequired,Email
from models import *

app = Flask(__name__)


class InsertDataForm(FlaskForm):
    name = StringField("Name: ",validators=[DataRequired()])
    age = IntegerField("Age: ",validators=[DataRequired()])
    email = EmailField("Email: ",validators=[DataRequired(),Email()])
    city = StringField("City: ",validators=[DataRequired()])
    submit = SubmitField("Submit")




@app.route("/",methods=["GET","POST"])
def index():
    form = InsertDataForm()
    if form.validate_on_submit():
        user = InsertData(name=form.name.data, age=form.age.data, email=form.email.data, city=form.city.data)
        db.create_all()
        db.session.add(user)
        db.session.commit()
    return jsonify(message = "Successfully added",status = 200)
    # return render_template('index.html',form=form)

@app.route("/Users")
def Users():
    Users = InsertData.query.all()
    print(Users)
    return "Hello"
if __name__ == "__main__":
    app.run(debug=True)