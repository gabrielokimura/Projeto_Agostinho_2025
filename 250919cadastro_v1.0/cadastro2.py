from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort,flash

app = Flask(__name__)

app.config['SECRET_KEY'] = "456743785t24783564738564783"




@app.route("/area-restrita")
def area_restrita():
    print ("Tentativa de acesso à área restrita sem autorização.")
    abort(401)




@app.route("/painel-admin")
def painel_admin():

    #aqui haveria uma verificação para ver se o usuário logado é um administrador

    print("Tentativa de acesso ao painel de administradorin sem permissão.")
    abort(403)
    
    
@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("error404.html"), 404




@app.errorhandler(401)
def nao_autorizado(error):
    return render_template("error401.html"), 401




@app.errorhandler(403)
def acesso_proibido(error):
    return render_template("error403.html"),403         

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
            flash(f"Obrigado por se cadastrar, {session["usuario"]}!", "success")
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