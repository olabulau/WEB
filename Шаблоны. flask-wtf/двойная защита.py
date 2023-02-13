from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    userid = SubmitField('Id austranaut', validators=[DataRequired()])
    password_1 = PasswordField('Password austranaut', validators=[DataRequired()])
    cap_id = SubmitField('Id capitan', validators=[DataRequired()])
    password_2 = PasswordField('Password capitan', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/')
def index():
    return redirect('/login')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')