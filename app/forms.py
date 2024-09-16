from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username    = StringField  ('username', validators=[DataRequired()])
    password    = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField ('remember me')
    submit      = SubmitField  ('Login')

class PropertyForm(FlaskForm):
    type   = SelectField (label='Property Type', choices=[('house', 'House'), ('apartment', 'Apartment')], default='house')
    submit = SubmitField ('Next')

class HouseForm(FlaskForm):
    square_footage    = FloatField('Square Footage', validators=[DataRequired()])
    num_of_bedrooms   = IntegerField('Number of bedrooms', validators=[DataRequired()])
    num_of_bathrooms  = IntegerField('Number of bathrooms', validators=[DataRequired()])
    parking           = SelectField (label='Parking', choices=[('yes', 'Yes'), ('no', 'No')], default='No')
    private_pool      = SelectField (label='Private pool', choices=[('yes', 'Yes'), ('no', 'No')], default='No')
    exterior_features = SelectField (label='Exterior features', choices=[('yes', 'Yes'), ('no', 'No')], default='No')
    submit = SubmitField ('Add')

class ApartmentForm(FlaskForm):
    square_footage        = FloatField('Square footage', validators=[DataRequired()])
    num_of_bedrooms       = IntegerField('Number of bedrooms', validators=[DataRequired()])
    num_of_bathrooms      = IntegerField('Number of bathrooms', validators=[DataRequired()])
    balcony               = SelectField(label='balcony', choices=[('yes','Yes'), ('no',"No")], default='No')
    rentable_storage_unit = SelectField(label='Rentable storage unit', choices=[('yes','Yes'),('no','No')], default='No')
    fully_renovated_house = SelectField(label='Fully renovated house', choices=[('yes','Yes'),('no','No')], default='No')
    submit                = SubmitField('Add')

class PropertyListing(FlaskForm):
    status = SelectField(label= 'Status', choices=[('available','Available'), ('sold', 'Sold'), ('rented','Rented')], default="Available")
    submit = SubmitField('Edit')





