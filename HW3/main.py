# Задание
#
# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.


from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from markupsafe import escape

from models import db, User
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

app.config['SECRET_KEY'] = b'ea959bc6bbd140100d66503aa6ac1242c6eb0e8d4c38b85c7ea9a9d2a8e60451'

csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi!'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    # print('OK')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username, password) in db():
            return "Вы вошли "
        return f'неправильный {escape(username)} логин или пароль'
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter((User.name == name) | (User.email == email)).first()

        if existing_user:
            error_msg = 'Username or email already exists.'
            form.name.errors.append(error_msg)
            return render_template('register.html', form=form)

        user = User(name=name, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return 'Registered success!'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
