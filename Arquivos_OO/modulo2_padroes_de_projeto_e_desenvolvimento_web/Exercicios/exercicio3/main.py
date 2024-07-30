from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Exemplo de variáveis que você pode passar para o template
    titulo = "Exemplo de Flask"
    numeros = [1, 2, 3, 4, 5]
    return render_template('index.html', titulo=titulo, numeros=numeros)

if __name__ == '__main__':
    app.run(debug=True)