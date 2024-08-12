from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username    = StringField  ('username', validators=[DataRequired()])
    password    = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField ('remember me')
    submit      = SubmitField  ('Login')
<<<<<<< HEAD

class PropertyForm(FlaskForm):
    type = SelectField (label='Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], default='house')
    submit = SubmitField ('Next')
=======
>>>>>>> d3b8372551b1579872a96246d55b0f413d38fa11
