from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort,flash, jsonify
from models import *



app = Flask(__name__)

app.config['SECRET_KEY'] = "456743785t24783564738564783"


@app.route("/")
def pagina_inicial():
    sessao =Sessao()
    carros = sessao.query(Veiculo).all() 
    modelos = sessao.query(Modelo).all()
    marcas = sessao.query(Marca).all()
    if session.get("funcionario_id"):
        funcionario = sessao.query(Funcionario).filter_by(id = session.get("funcionario_id")).first()
        if funcionario:
            cargo = funcionario.cargo
        else:
            cargo=None 
    else:
        cargo=None 
    sessao.close()
             
    return render_template("pagina_inicial.html", carros_cadastrados=carros, cargo = cargo, modelos = modelos, marcas = marcas)



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
    sessao =Sessao()
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
            cadastrar_cliente( session["nome"], session["email"],session["senha"],session["data_nasc"], session["cnh"], session["cpf"], session["doc_identificacao"], session["telefone"])
            flash(f'Obrigado por se cadastrar, {session["nome"]}!', "success")
            return redirect(url_for("login"))
        else:
            mensagem = "Bota o nome E a senha idiota"


    return render_template("cadastro.html", mensagem = mensagem, usuarios = sessao.query(Cliente).all())

@app.route("/login", methods = ["GET", "POST"])
def login():
    sessao=Sessao()
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


@app.route("/<int:carro_id>")
def detalhar_carro(carro_id):
    sessao =Sessao()
    carro = sessao.query(Veiculo).filter_by(id=carro_id).first()
    if carro is None:
        abort(404)
    return render_template("detalhar_carro.html", carro= carro) 




@app.route("/receber_carro", methods=["POST"])
def receber_carro():
    print("Recebendo dados do carro...") 
    try:
        lista_de_atributos = request.get_json()
        print(f"Dados recebidos: {lista_de_atributos}")  
        resultado = cadastrar_carro(*lista_de_atributos)
        if "Erro" in resultado:
            print(f"Erro no cadastro: {resultado}")  
            return jsonify({"success": False, "message": resultado}), 400
        print("Carro cadastrado com sucesso!")  
        return jsonify({"success": True, "message": resultado})
    except Exception as erro:
        print(f"Erro na rota: {erro}")  
        return jsonify({"success": False, "message": "Erro interno"}), 500








@app.route("/pegar_lista")
def pegar_lista():
    sessao = Sessao()
    try:
        carros = sessao.query(Veiculo).all()
        lista_carros = []
        for carro in carros:
            marca = sessao.query(Marca).filter_by(id= carro.id_marca).first()
            if not marca:
                return "Marca não encontrada"
            modelo = sessao.query(Modelo).filter_by(id= carro.id_modelo).first()
            if not modelo:
                return "Modelo não encontrado"
            combustivel = sessao.query(Combustivel).filter_by(id= carro.id_combustivel).first()
            if not combustivel:
                return "Combustível não encontrado"
            categoria = sessao.query(Categoria).filter_by(id= carro.id_categoria).first()
            if not categoria:
                return "Categoria não encontrada"
            fornecedor = sessao.query(Fornecedor).filter_by(id = carro.id_fornecedor).first()
            if not fornecedor:
                return "Fornecedor não encontrado"
            garagem = sessao.query(Garagem).filter_by(id= carro.id_garagem).first()
            if not garagem:
                return "Garagem não encontrada"
            plano_seguro = sessao.query(PlanoSeguro).filter_by(id= carro.id_plano_seguro).first()
            if not plano_seguro:
                return "plano de seguro não encontrado"
            lista_carros.append(
                {
                "id": carro.id,
                "placa": carro.placa,
                "marca": marca.nome,  
                "modelo": modelo.nome,
                "preco_diaria": float(carro.preco_diaria),
                "cor": carro.cor,
                "cambio": carro.cambio,
                "portas": carro.portas,
                "airbags": carro.airbags,
                "ar_condicionado": carro.ar_condicionado,
                "quilometragem": carro.quilometragem,
                "combustivel": combustivel.tipo,
                "categoria": categoria.nome,
                "preco_compra": float(carro.preco_compra),
                "capacidade_pessoas": carro.capacidade_pessoas,
                "fornecedor": fornecedor.nome,
                "garagem": garagem.logradouro,
                "plano_seguro": plano_seguro.tipo
            }
            )
        return jsonify(lista_carros)
    finally:
        sessao.close()



@app.route("/comprar_carro", methods = ["POST"])
def comprar_carro():
    if request.method=="POST":
        try:
            local_entrega = request.form.get("local_entrega")
            horario_entrega = request.form.get("horario_entrega")
            local_devolucao = request.form.get("local_devolucao")
            horario_devolucao = request.form.get("horario_devolucao")
            metodo_pagamento = request.form.get("metodo_pagamento")
            session["local_entrega"] = local_entrega
            session["horario_entrega"] = horario_entrega
            session["local_devolucao"] = local_devolucao
            session["horario_devolucao"] = horario_devolucao
            session["metodo_pagamento"] = metodo_pagamento
            carro_id = request.form.get("carro_id")
            session["carro_id"] = carro_id
            return redirect(url_for("confirmar_compra"))
        except Exception as e:
            print(e)


@app.route("/confirmar_compra")
def confirmar_compra():
    metodo_pagamento = session.get("metodo_pagamento")
    carro_id = session.get("carro_id")
    sessao =Sessao()
    if not metodo_pagamento or not carro_id:
        return redirect(url_for("pagina_inicial"))
    carro = sessao.query(Veiculo).filter_by(id =carro_id).first()
    formato = "%Y-%m-%dT%H:%M"
    horario_entrega =session.get("horario_entrega")
    horario_devolucao=session.get("horario_devolucao")
    horario_entrega = datetime.strptime(horario_entrega, formato)
    horario_devolucao =datetime.strptime(horario_devolucao, formato)
    diferenca = horario_devolucao - horario_entrega
    diferenca_dias = diferenca.days

    return render_template("confirmar_compra.html", metodo_pagamento = metodo_pagamento, dias= diferenca_dias, preco_diaria=carro.preco_diaria)

@app.route("/comprar_definitivo", methods=["POST"])
def comprar_definitivo():
    metodo_pagamento = session.get("metodo_pagamento")
    if not metodo_pagamento:
       return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        sessao =Sessao()
        carro_id =session.get("carro_id")
        carro = sessao.query(Veiculo).filter_by(id=carro_id).first()
        if carro.disponivel == True:
            carro.disponivel = False
            sessao.commit()
        sessao.close()
        return redirect(url_for("pagina_inicial"))


if __name__=="__main__":
    app.run(debug=True)


