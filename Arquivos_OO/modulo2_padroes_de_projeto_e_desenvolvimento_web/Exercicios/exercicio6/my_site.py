from flask import Flask, render_template

app = Flask(__name__)

#cria a primeira pagina do site

# route -> hashtagtreinamentos.com/oquevemdepoisdabarra
# função -> oque você quer exibir naquela página
@app.route("/") 
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return nome_usuario

@app.route("/formulario")
def formulario():
    return render_template ("formulario.html")


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
 
