from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curso', methods=['GET', 'POST'])
def curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return f"Nombre: {nombre}<br>Apellidos: {apellidos}<br>Curso: {curso}"
    return render_template('curso.html')

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        password = request.form['password']
        return f"Usuario: {nombre} {apellidos}<br> Email: {email}"
    return render_template('usuarios.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f"Producto: {producto}<br>Categoría: {categoria}<br>Existencia: {existencia}<br>Precio: {precio}"
    return render_template('productos.html')

@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        modo = request.form['modo']
        return f"Título: {titulo}<br>Autor: {autor}<br>Resumen: {resumen}<br>Modo: {modo}"
    return render_template('libros.html')

if __name__ == '__main__':
    app.run(debug=True)


