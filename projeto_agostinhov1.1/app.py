from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort,flash, jsonify
from models import *



app = Flask(__name__)

app.config['SECRET_KEY'] = "456743785t24783564738564783"


@app.route("/")
def pagina_inicial():
    if session.get("funcionario_id"):
        funcionario = sessao.query(Funcionario).filter_by(id = session.get("funcionario_id")).first()
        cargo = funcionario.cargo
    else:
        cargo=None       
    return render_template("pagina_inicial.html", carros_cadastrados=sessao.query(Veiculo).all(), cargo = cargo)


@app.route("/pegar_lista")
def get_carros():
    return jsonify(sessao.query(Veiculo).all())


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
        session["doc_identificacao"] = request.form.get("doc_identificacao")
        if session["nome"] and session["email"] and session["senha"] and session["telefone"] and session["data_nasc"] and session["cpf"] and session["cnh"] and session["doc_identificacao"]:
            cadastrar_cliente(session["nome"], session["nome"], session["email"],session["senha"],session["data_nasc"], session["cnh"], session["cpf"], session["doc_identificacao"])
            flash(f'Obrigado por se cadastrar, {session["nome"]}!', "success")
            return redirect(url_for("login"))
        else:
            mensagem = "Bota o nome E a senha idiota"


    return render_template("cadastro.html", mensagem = mensagem, usuarios = sessao.query(Cliente).all())

@app.route("/login", methods = ["GET", "POST"])
def login():
    mensagem = ""
    if request.method=="POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        print(nome)
        print(senha)
        try:
            cliente = sessao.query(Cliente).filter_by(nome=nome, senha=senha).first()
            if cliente:
                session["nome"] = cliente.nome
                session["senha"] = cliente.senha
                session["cliente_id"] = cliente.id
                session["cargo"] = "cliente"  
                sessao.close()
                return redirect(url_for("pagina_inicial"))
            
            funcionario = sessao.query(Funcionario).filter_by(nome=nome, senha=senha).first()  
            print(funcionario.nome)
            if funcionario:
                session["nome"] = funcionario.nome
                session["senha"] = funcionario.senha
                session["funcionario_id"] = funcionario.id
                session["tipo"] = "funcionario" 
                sessao.close()
                return redirect(url_for("pagina_inicial"))
            

            mensagem = "Usúario ou senha incorretos"
        except Exception as e:
            mensagem = f"Ocorreu um erro: {str(e)}" 
        finally:
            sessao.close() 
    return render_template("login.html", mensagem=mensagem)
        

    
       
                
                
        


@app.route("/logout")
def logout():
    session.clear()     
    return redirect(url_for("pagina_inicial"))



@app.route("/receber_carro", methods = ["POST"])
def receber_carro():
    try:
        lista_de_atributos = request.get_json()
        cadastrar_carro(*lista_de_atributos) 
        return jsonify({"success": True, "message": "Carro cadastrado com sucesso!"})
    except Exception as erro:
        return jsonify({"success": False, "message": str(erro)}), 500
        
        

@app.route("/perfil")
def perfil():
    usuario = session.get("usuario")
    if usuario:
        return render_template("perfil.html", usuario = usuario)
    else:
        return abort(401)


@app.route("/cadastro_carro")
def cadastro_carro():
    return render_template("cadastro_carro.html")


""" @app.route("/<int:carro_id>")
def detalhar_carro(carro_id):
    carro = modelo.achar_carro(carro_id)
    if carro is None:
        abort(404)
    return render_template("detalhar_carro.html", carro= carro) """




if __name__=="__main__":
    app.run(debug=True)