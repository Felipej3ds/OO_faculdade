from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\felip\OneDrive\Área de Trabalho\terceiro semestre\OO\Arquivos_OO\modulo2\Exercicios\Exercicio5.5\upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + r'C:\Users\felip\OneDrive\Área de Trabalho\terceiro semestre\OO\Arquivos_OO\modulo2\Exercicios\Exercicio5.5\Upload\bancodedados.db'
app.secret_key = "your_secret_key"

db = SQLAlchemy(app)
app.app_context().push()

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    senha = db.Column(db.String)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

@app.route("/usuario", methods=['POST', 'GET'])
def addUsuario():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        user = Usuario(nome, senha)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('formulario'))
    users = Usuario.query.all()
    return render_template('usuario.html', usuarios=users)

@app.route("/formulario", methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        user = Usuario.query.filter_by(nome=nome, senha=senha).first()
        if user:
            return redirect(url_for('upload'))
    return render_template('formulario.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['arquivo']
        savePath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(savePath)
        return 'Upload feito com sucesso'
    return render_template('upload.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
