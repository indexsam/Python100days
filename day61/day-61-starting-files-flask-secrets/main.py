from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from flask_bootstrap import Bootstrap5


# pip install email_validator ( for wtf Email() to work)

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20) ])
    submit = SubmitField('Log In')

app = Flask(__name__)
app.secret_key = "some secret string"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form=MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        if form.email.data=="obadansam@gmail.com" and form.password.data == "12345678":
            return redirect("/success")
        else:
            return redirect("/denied")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

# pip install bootstrap-flask  (NOTE this addition for additional templating)