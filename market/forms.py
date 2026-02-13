from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User, Item


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')


class AddItemForm(FlaskForm):
    name = StringField(label='Item Name', validators=[Length(min=2, max=30), DataRequired()])
    price = StringField(label='Price', validators=[DataRequired()])
    barcode = StringField(label='Barcode', validators=[Length(min=8, max=12), DataRequired()])
    description = StringField(label='Description', validators=[Length(min=2), DataRequired()])
    submit = SubmitField(label='Add Item')

    def validate_name(self, name_to_check):
        item = Item.query.filter_by(name=name_to_check.data).first()
        if item:
            raise ValidationError('An item with that name already exists.')

    def validate_barcode(self, barcode_to_check):
        item = Item.query.filter_by(barcode=barcode_to_check.data).first()
        if item:
            raise ValidationError('An item with that barcode already exists.')


class AddFundsForm(FlaskForm):
    amount = StringField(label='Amount', validators=[DataRequired()])
    submit = SubmitField(label='Add Funds')