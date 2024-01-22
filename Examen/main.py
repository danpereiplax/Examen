from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class PurchaseForm:
    def __init__(self, name, age, quantity):
        self.name = name
        self.age = age
        self.quantity = quantity

def calculate_totals(name, age, quantity):
    paint_price = 9000
    total_without_discount = quantity * paint_price

    if 18 <= age <= 30:
        discount = 0.15
    elif age > 30:
        discount = 0.25
    else:
        discount = 0

    total_with_discount = total_without_discount - (total_without_discount * discount)

    return total_without_discount, total_with_discount

def authenticate_user(username, password):
    users = {
        'juan': 'admin',
        'pepe': 'user'
    }

    if username in users and users[username] == password:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise1', methods=['GET', 'POST'])
def exercise1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        quantity = int(request.form['quantity'])

        total_without_discount, total_with_discount = calculate_totals(name, age, quantity)

        return render_template('calculocompras.html', name=name, total_without_discount=total_without_discount, total_with_discount=total_with_discount)

    return render_template('calculocompras.html')  # Mostrar el formulario inicial

@app.route('/exercise2', methods=['GET', 'POST'])
def exercise2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            if username == 'juan':
                welcome_message = 'Bienvenido administrador juan'
            elif username == 'pepe':
                welcome_message = 'Bienvenido usuario pepe'
            else:
                welcome_message = 'Bienvenido ' + username
        else:
            welcome_message = 'Usuario o contraseña incorrectos'

        return render_template('calculousuarios.html', welcome_message=welcome_message)

    return render_template('calculousuarios.html')  # Mostrar el formulario inicial

if __name__ == '__main__':
    app.run(debug=True)
