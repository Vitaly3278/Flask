# 1) Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# 2) При отправке которой будет создан cookie файл с данными
# пользователя
# 3) Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# 4) На странице приветствия должна быть кнопка "Выйти"
# 5) При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '6d0d6a76c0e1522467f9cc1681db0a5472bd1c30a03832d1af4b71f3816d8f84'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/loginit/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()