from flask import Flask, render_template, redirect, url_for, request, make_response, session

app = Flask(__name__)

app.secret_key="123"            

usuarios_cadastrados=[]
senhas_cadastradas=[]

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    mensagem= ""
    if request.method=="POST":
        session["usuario"]=request.form.get("nome")
        session["senha"] = request.form.get("senha")
        if session["usuario"] and session["senha"]:
            usuarios_cadastrados.append(session["usuario"])
            senhas_cadastradas.append(session["senha"])
            return redirect(url_for("login"))
        else:
            mensagem = "Bota o nome E a senha idiota"


    return render_template("cadastro.html", mensagem = mensagem, usuarios = usuarios_cadastrados)

@app.route("/login", methods = ["GET", "POST"])
def login():
    mensagem = ""
    if request.method=="POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        tamanho = len(usuarios_cadastrados)
        for i in range (tamanho):
            if nome == usuarios_cadastrados[i] and senha == senhas_cadastradas[i]:
                session["nome"] = usuarios_cadastrados[i]
                return redirect(url_for("logado"))
        mensagem = "Usúario ou senha incorretos"
    return render_template("login.html", mensagem=mensagem)
        

@app.route("/logado")
def logado():
    nome = session.get("nome")
    if not nome:
        return redirect(url_for("login"))
    return render_template("logado.html", nome=nome)

@app.route("/logout")
def logout():
    session.clear()     
    return redirect(url_for("login"))


if __name__=="__main__":
    app.run(debug=True)