from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados/database.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(50), nullable=False)

db.create_all()

@app.route("/formulario", methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(nome=nome, senha=senha).first()
        if usuario:
            return redirect(url_for('outra_rota'))
        else:
            return render_template('formulario.html', mensagem="Usuário ou senha inválidos.")
    else:
        return render_template('formulario.html')

@app.route("/outra_rota")
def outra_rota():
    return render_template('outra_rota.html')

if __name__ == '__main__':
    app.run(debug=True)