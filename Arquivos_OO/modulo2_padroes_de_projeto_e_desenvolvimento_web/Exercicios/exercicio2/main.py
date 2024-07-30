from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<nome>')
def ola_mundo(nome):
    return render_template("index.html", visitante=nome)

@app.route('/formulario/<nome>')
def formulario(nome):
    return render_template("formulario.html", visitante=nome)

if __name__ == '__main__':
    app.run()