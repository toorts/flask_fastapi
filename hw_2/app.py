from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    # Получаем данные из формы
    name = request.form.get('name')
    email = request.form.get('email')

    # Создаем cookie с данными пользователя
    response = make_response(redirect('/greet'))
    response.set_cookie('user_data', f'{name},{email}')
    
    return response

@app.route('/greet')
def greet():
    # Получаем данные из cookie
    user_data = request.cookies.get('user_data')

    if user_data:
        name, _ = user_data.split(',')
        return render_template('welcome.html', name=name)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    # Удаляем cookie с данными пользователя
    response = make_response(redirect('/'))
    response.delete_cookie('user_data')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
