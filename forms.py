from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectMultipleField, SelectField
from wtforms.validators import InputRequired, EqualTo, DataRequired

class RegistrationForm(FlaskForm):
    user_id = StringField("User id: ",
        validators=[InputRequired()])
    password = PasswordField("Password: ",
        validators=[InputRequired()])
    password2 = PasswordField("Repeat password: ",
        validators=[InputRequired(), EqualTo("password", message="Passwords must match")])
    submit = SubmitField("Submit")
    
class LoginForm(FlaskForm):
    user_id = StringField("User id: ",
        validators=[InputRequired()])
    password = PasswordField("Password: ",
        validators=[InputRequired()])
    submit = SubmitField("Submit")

class CreateTimetableForm(FlaskForm):
    course = SelectMultipleField('Course', validators=[DataRequired()], choices=[
        ("CS1110", "CS1110"),
        ('CS1113', 'CS1113'),
        ('CS1116', 'CS1116'),
        ('CS1117', 'CS1117'),
        ('MA1002', 'MA1002'),
        ('Tennis', 'Tennis'),
        ('Soccer', 'Soccer')
    ])
    submit = SubmitField('Submit')






# class SearchForm(FlaskForm):
#     search_query = StringField("Search: ", validators=[InputRequired()])
#     activity_type = SelectField("")
