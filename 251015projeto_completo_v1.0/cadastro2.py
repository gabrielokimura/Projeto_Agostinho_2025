from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort,flash, jsonify

app = Flask(__name__)

app.config['SECRET_KEY'] = "456743785t24783564738564783"

carros_cadastrados = []


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

usuarios_cadastrados=[{"nome":"Admin123", "senha":"123", "admin":True}]


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    mensagem= ""
    if request.method=="POST":
        session["nome"]=request.form.get("nome")
        session["senha"] = request.form.get("senha")
        session["email"] = request.form.get("email")
        session["telefone"] = request.form.get("telefone")
        session["data_nasc"] = request.form.get("data_nasc")
        session["cpf"] = request.form.get("cpf")
        session["cnh"] = request.form.get("cnh")
        if session["nome"] and session["senha"] and session["email"] and session["telefone"] and session["data_nasc"] and session["cpf"] and session["cnh"]:
            usuarios_cadastrados.append({"nome":session["nome"], "senha":session["senha"],"email":session["email"],"telefone":session["telefone"], "data_nasc":session["data_nasc"], "cpf":session["cpf"],"cnh":session["cnh"] , "admin":False})
            flash(f"Obrigado por se cadastrar, {session["nome"]}!", "success")
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
            if nome == usuarios_cadastrados[i]["nome"] and senha == usuarios_cadastrados[i]["senha"]:
                session["nome"] = usuarios_cadastrados[i]["nome"]
                session["senha"] = usuarios_cadastrados[i]["senha"]
                session["usuario"] = usuarios_cadastrados[i]
                return redirect(url_for("logado"))
        mensagem = "Usúario ou senha incorretos"
    return render_template("login.html", mensagem=mensagem)
        

@app.route("/logado")
def logado():
    usuario = session.get("usuario")
    if not usuario:
        return abort(401)
    return render_template("logado.html", usuario = usuario, carros_cadastrados=carros_cadastrados)

@app.route("/logout")
def logout():
    session.clear()     
    return redirect(url_for("login"))



@app.route("/receber_carro", methods = ["POST"])
def receber_carro():
    try:
        novo_carro = request.get_json()
        carros_cadastrados.append(novo_carro)
        return jsonify({"success": True, "message": "Carro cadastrado com sucesso!"})
    except Exception as erro:
        return jsonify({"success": False, "message": str(erro)}), 500
        
        

@app.route("/logado/perfil")
def perfil():
    usuario = session.get("usuario")
    if usuario:
        return render_template("perfil.html", usuario = usuario)
    else:
        return abort(401)


@app.route("/cadastro_carro")
def cadastro_carro():
    usuario = session.get("usuario")
    
    if usuario == None or not usuario["admin"]:
        return abort(403)
    return render_template("cadastro_carro.html")


if __name__=="__main__":
    app.run(debug=True)