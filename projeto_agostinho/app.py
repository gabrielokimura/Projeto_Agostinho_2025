from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort,flash, jsonify
from models import Modelo

modelo = Modelo()

app = Flask(__name__)

app.config['SECRET_KEY'] = "456743785t24783564738564783"



@app.route("/pegar_lista")
def get_carros():
    return jsonify(modelo.carros_cadastrados)


@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("error404.html"), 404




@app.errorhandler(401)
def nao_autorizado(error):
    return render_template("error401.html"), 401




@app.errorhandler(403)
def acesso_proibido(error):
    return render_template("error403.html"),403         



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
            modelo.cadastrar_usuario(session["nome"], session["senha"], session["email"], session["telefone"],session["data_nasc"], session["cpf"], session["cnh"])
            flash(f'Obrigado por se cadastrar, {session["nome"]}!', "success")
            return redirect(url_for("login"))
        else:
            mensagem = "Bota o nome E a senha idiota"


    return render_template("cadastro.html", mensagem = mensagem, usuarios = modelo.usuarios_cadastrados)

@app.route("/login", methods = ["GET", "POST"])
def login():
    mensagem = ""
    if request.method=="POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        tamanho = len(modelo.usuarios_cadastrados)
        for i in range (tamanho):
            if nome == modelo.usuarios_cadastrados[i]["nome"] and senha == modelo.usuarios_cadastrados[i]["senha"]:
                session["nome"] = modelo.usuarios_cadastrados[i]["nome"]
                session["senha"] = modelo.usuarios_cadastrados[i]["senha"]
                session["usuario"] = modelo.usuarios_cadastrados[i]
                return redirect(url_for("logado"))
        mensagem = "Usúario ou senha incorretos"
    return render_template("login.html", mensagem=mensagem)
        

@app.route("/logado")
def logado():
    usuario = session.get("usuario")
    if not usuario:
        return abort(401)
    return render_template("logado.html", usuario = usuario, carros_cadastrados=modelo.carros_cadastrados)

@app.route("/logout")
def logout():
    session.clear()     
    return redirect(url_for("login"))



@app.route("/receber_carro", methods = ["POST"])
def receber_carro():
    try:
        novo_carro = request.get_json()
        modelo.cadastrar_carro(novo_carro)
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


@app.route("/logado/<int:carro_id>")
def detalhar_carro(carro_id):
    carro = modelo.achar_carro(carro_id)
    if carro is None:
        abort(404)
    return render_template("detalhar_carro.html", carro= carro)




if __name__=="__main__":
    app.run(debug=True)