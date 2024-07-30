from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\felip\OneDrive\Área de Trabalho\terceiro semestre\OO\Arquivos_OO\modulo2\Exercicios\Exercicio5.5\upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + r'C:\Users\felip\OneDrive\Área de Trabalho\terceiro semestre\OO\Arquivos_OO\modulo2\Exercicios\Exercicio5.5\Upload\bancodedados.db'
app.secret_key = "sua_chave_secreta"

db = SQLAlchemy(app)
app.app_context().push()

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    senha = db.Column(db.String)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = generate_password_hash(senha)  # Hash da senha

@app.route("/usuario", methods=['POST', 'GET'])
def addUsuario():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        if Usuario.query.filter_by(nome=nome).first():
            flash("Usuário já existe.")
            return redirect(url_for('addUsuario'))
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
        user = Usuario.query.filter_by(nome=nome).first()
        if user and check_password_hash(user.senha, senha):
            session['user_id'] = user.id
            return redirect(url_for('upload'))
        flash("Nome de usuário ou senha inválidos.")
    return render_template('formulario.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if 'user_id' not in session:
        return redirect(url_for('formulario'))
    if request.method == 'POST':
        file = request.files['arquivo']
        if file:
            savePath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(savePath)
            return 'Upload feito com sucesso'
        flash("Nenhum arquivo selecionado para upload.")
    return render_template('upload.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)