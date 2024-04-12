from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, SubmitField, StringField, BooleanField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = StringField("e-mail",
                        validators=[InputRequired("É obrigatório indicar o email")])
    password = PasswordField("Senha",
                             validators=[InputRequired("Informe a sua senha")])
    remember_me = BooleanField("Lembrar de mim?")
    submit = SubmitField("Logar no sistema")