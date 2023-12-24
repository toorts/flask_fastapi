from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data
        )  # type: ignore
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Вы успешно зарегистрированы!', 'success')
        return redirect(url_for('register'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
