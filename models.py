from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange
from currencies import create_currency_list

currency_list = create_currency_list()


class ConvertForm(FlaskForm):
    to = SelectField("To", choices=currency_list, validators=[DataRequired()], default='GBP')
    from_ = SelectField("From", choices=currency_list, validators=[DataRequired()], default='EUR')
    amount = IntegerField("Amount", validators=[DataRequired(), NumberRange(min=1)], default=1)
    submit = SubmitField("Calculate")
