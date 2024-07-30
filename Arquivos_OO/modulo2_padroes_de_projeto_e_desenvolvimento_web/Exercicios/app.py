from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Função para criar a tabela de logins no banco de dados
def create_table():
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logins (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Função para inserir um novo login no banco de dados
def insert_login(username, password):
    conn = sqlite3.connect('logins.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logins (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

# Rota para a página de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para lidar com o envio do formulário de cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        insert_login(username, password)
        return redirect('/upload')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)