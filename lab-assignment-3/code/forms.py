from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField
from wtforms.fields.html5 import EmailField


# Form to add contact to database.
# This for is rendered on the frontend for the user.
class addContactForm(FlaskForm):
    name = StringField("Name:", [validators.DataRequired()])
    mobile_no = StringField("Mobile No:", [validators.DataRequired()])
    email = EmailField("Email:", [validators.DataRequired()])
    submit = SubmitField('Add Contact!')
