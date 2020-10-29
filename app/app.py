from flask import Flask, render_template, redirect, url_for, request
import csv

def guardar_datos(nombre,email,wifi,telefono):
    archivo = open('datos/datos_formulario.csv', 'a')
    archivo.write("{},{},{},{}\n".format(nombre,email,wifi,telefono))
    archivo.close()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form', methods=["POST"])
def form():
    nombre = request.form.get("name")
    email = request.form.get("email")
    wifi = request.form.get("planes")
    telefono = request.form.get("phone")

    mensaje = "¡Se envió el formulario con éxito! Pronto lo contactaremos."
    guardar_datos(nombre,email,wifi,telefono)
    return render_template("index.html", mensaje=mensaje)

@app.route('/login_empleados', methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Credenciales inválidas. Intente nuevamente."
        else:
            return redirect(url_for('datos'))
    return render_template("login.html", error=error)

@app.route('/datos')
def datos():
    with open('datos/datos_formulario.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        clientes = []
        for row in data:
            clientes.append({
            "nombre": row[0],
            "email": row[1],
            "plan": row[2],
            "tel": row[3]
            })
    return render_template("datos.html", clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    