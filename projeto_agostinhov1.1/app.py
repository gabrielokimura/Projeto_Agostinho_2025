from flask import Flask, render_template, redirect, url_for, request, make_response, session, abort,flash, jsonify
from models import *



app = Flask(__name__)

app.config['SECRET_KEY'] = "456743785t24783564738564783"


@app.route("/", methods=["GET","POST"])
def pagina_inicial():
    sessao =Sessao()
    carros_filtrados_ids = session.get("carros_filtrados_ids")
    if carros_filtrados_ids==[]:
        carros = []
        mensagem = "Sua filtragem não encontrou resultados, tente outra combinção de filtragem"
        print("Nenhum carro cumpre os filtros") 
    elif carros_filtrados_ids is not None:
        carros = sessao.query(Veiculo).filter(Veiculo.id.in_(carros_filtrados_ids)).all()
        print("OIIIIIIIIIIIII")
        mensagem = ""
    else:
        carros = sessao.query(Veiculo).all() 
        mensagem=""
    
    modelos = sessao.query(Modelo).all()
    marcas = sessao.query(Marca).all()
    garagens = sessao.query(Garagem).all()
    local_retirada = session.get("local_retirada")
    valor_maximo = session.get("valor_maximo")
    valor_minimo = session.get("valor_minimo")
    porta = session.get("porta")
    cambio = session.get("cambio")
    marca = session.get("marca")
    modelo = session.get("modelo")
    usuario = session.get("id_usuario")
    if session.get("cargo"):
        funcionario = sessao.query(Funcionario).filter_by(id = session.get("id_usuario")).first()
        if funcionario:
            cargo = funcionario.cargo
        else:
            cargo=None 
    else:
        cargo=None 
    sessao.close()
             
    return render_template("pagina_inicial.html", carros_cadastrados=carros, cargo = cargo, modelos = modelos, marcas = marcas, garagens = garagens, local_retirada=local_retirada,valor_maximo=valor_maximo,valor_minimo=valor_minimo,porta=porta,cambio=cambio,modelo=modelo,marca=marca, mensagem=mensagem, usuario = usuario)


@app.route("/filtrar", methods = ["GET","POST"])
def filtrar():
    if request.method == "POST":
        sessao = Sessao()
        local_retirada = request.form.get("local_retirada")
        valor_maximo = request.form.get("maximo")
        valor_minimo = request.form.get("minimo")
        porta = request.form.get("porta")
        cambio = request.form.get("cambio")
        modelo = request.form.get("modelo")
        marca = request.form.get("marca")
        if not local_retirada and not valor_maximo and not valor_minimo and  not porta and not cambio and not modelo and not marca:
            session.pop("local_retirada", None)
            session.pop("valor_maximo", None)
            session.pop("valor_minimo", None)
            session.pop("porta", None)
            session.pop("cambio", None)
            session.pop("modelo", None)
            session.pop("marca", None)
            session.pop("carros_filtrados_ids", None)
            sessao.close()
            return redirect(url_for("pagina_inicial"))
        else:
            if valor_maximo:
                valor_maximo = float(valor_maximo)
            if valor_minimo:
                valor_minimo=float(valor_minimo)
            if porta:
                porta =int(porta)
            query = sessao.query(Veiculo)
            if local_retirada:
                query = query.filter(Veiculo.id_garagem == local_retirada)
            if valor_maximo:
                query = query.filter(Veiculo.preco_diaria<=valor_maximo)
            if valor_minimo:
                query = query.filter(Veiculo.preco_diaria>=valor_minimo)
            if porta:
                query = query.filter(Veiculo.portas == porta)
            if cambio:
                query = query.filter(Veiculo.cambio == cambio)
            if modelo:
                query = query.filter(Veiculo.id_modelo == modelo)
            if marca:
                query = query.filter(Veiculo.id_marca == marca)
            carros_filtrados = query.all()
            carros_filtrados_ids = [carro.id for carro in carros_filtrados]
            session["carros_filtrados_ids"] = carros_filtrados_ids
            sessao.close()
            return redirect(url_for("pagina_inicial"))
            


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
    usuario = session.get("id_usuario")
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


    return render_template("cadastro.html", mensagem = mensagem, usuarios = sessao.query(Cliente).all(), usuario = usuario)

@app.route("/login", methods = ["GET", "POST"])
def login():
    usuario = session.get("id_usuario")
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
                session.clear()
                session["nome"] = cliente.nome
                session["senha"] = cliente.senha
                session["id_usuario"] = cliente.id
                session["tipo"] = "cliente"  
                sessao.close()
                return redirect(url_for("pagina_inicial"))
            
            funcionario = sessao.query(Funcionario).filter_by(nome=nome, senha=senha).first()  
            if funcionario:
                session.clear()
                session["nome"] = funcionario.nome
                session["senha"] = funcionario.senha
                session["id_usuario"] = funcionario.id
                session["cargo"] = "funcionario" 
                sessao.close()
                return redirect(url_for("pagina_inicial"))
            

            mensagem = "Usúario ou senha incorretos"
        except Exception as e:
            mensagem = f"Ocorreu um erro: {str(e)}" 
        finally:
            sessao.close() 
    return render_template("login.html", mensagem=mensagem, usuario=usuario)
        

    
       
                
                
        


@app.route("/logout")
def logout():
    session.clear()     
    return redirect(url_for("pagina_inicial"))



        
        

@app.route("/perfil")
def perfil():
    sessao = Sessao()
    usuario = session.get("id_usuario")
    if session.get("cargo"):
        usuario_certo = sessao.query(Funcionario).filter_by(id = usuario).first()
    elif session.get("tipo"):
        usuario_certo = sessao.query(Cliente).filter_by(id = usuario).first()
    if usuario_certo:
        return render_template("perfil.html", usuario = usuario_certo)
    else:
        return abort(401)


@app.route("/cadastro_carro")
def cadastro_carro():
    usuario = session.get("id_usuario")
    return render_template("cadastro_carro.html", usuario = usuario)




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



@app.route("/<int:carro_id>",methods = ["POST", "GET"])
def detalhar_carro(carro_id):
    sessao =Sessao()
    usuario = session.get("id_usuario")
    if not usuario:
        return abort(401)
    carro = sessao.query(Veiculo).filter_by(id=carro_id).first()
    marca = sessao.query(Marca).filter_by(id = carro.id_marca).first().nome
    modelo = sessao.query(Modelo).filter_by(id = carro.id_modelo).first().nome
    combustivel = sessao.query(Combustivel).filter_by(id = carro.id_combustivel).first().tipo
    categoria = sessao.query(Categoria).filter_by(id = carro.id_categoria).first().nome
    avaliacoes = sessao.query(Avaliacao).filter_by(id_veiculo = carro.id ).all()
    garagem = sessao.query(Garagem).filter_by(id = carro.id_garagem).first()
    garagens = sessao.query(Garagem).all()
    if carro is None:
        abort(404)
    if request.method =="POST":
        try:
            session["horario_entrega"] = request.form.get("horario_entrega")
            session["horario_devolucao"] = request.form.get("horario_devolucao")
            session["local_devolucao"] = request.form.get("local_devolucao")
            session["carro_id"] = carro_id
            return redirect(url_for("resumo_pedido"))
        except Exception as e:
            print(e)
    return render_template("detalhar_carro.html", carro= carro, usuario = usuario, marca = marca, modelo = modelo, combustivel = combustivel, categoria = categoria, avaliacoes=avaliacoes, garagem = garagem, garagens = garagens) 





@app.route("/resumo_pedido",methods = ["POST", "GET"])
def resumo_pedido():
    usuario = session.get("id_usuario")
    if not usuario:
        return abort(401)
    carro_id = session.get("carro_id")
    sessao =Sessao()
    carro = sessao.query(Veiculo).filter_by(id =carro_id).first()
    marca = sessao.query(Marca).filter_by(id = carro.id_marca).first().nome
    modelo = sessao.query(Modelo).filter_by(id = carro.id_modelo).first().nome
    formato = "%Y-%m-%dT%H:%M"
    horario_entrega =session.get("horario_entrega")
    horario_devolucao=session.get("horario_devolucao")
    horario_entrega = datetime.strptime(horario_entrega, formato)
    horario_devolucao =datetime.strptime(horario_devolucao, formato)
    diferenca = horario_devolucao - horario_entrega
    diferenca_dias = diferenca.days
    valor_total = carro.preco_diaria*diferenca_dias
    
    if request.method == "POST":
        try:
            metodo_pagamento = request.form.get("metodo_pagamento")
            session["metodo_pagamento"] = metodo_pagamento
            return redirect(url_for("confirmar_compra"))
        except Exception as e:
            print(e)
        finally:
            sessao.close()
    return render_template("resumo_pedido.html", valor_total = valor_total, carro = carro, marca = marca, modelo = modelo, usuario = usuario)

@app.route("/confirmar_compra", methods = ["GET", "POST"])
def confirmar_compra():
    usuario = session.get("id_usuario")
    if not usuario:
        return abort(401)
    metodo_pagamento = session.get("metodo_pagamento")
    if not metodo_pagamento or not session.get("carro_id"):
        return redirect(url_for("pagina_inicial"))
    if request.method == "POST":
        return redirect(url_for("comprar_definitivo"))
           
    return render_template("confirmar_compra.html", metodo_pagamento = metodo_pagamento, usuario=usuario)



@app.route("/comprar_definitivo", methods=["POST"])
def comprar_definitivo():
    id_usuario = session.get("id_usuario")
    if not id_usuario:
        return abort(401)
    sessao = Sessao()
    carro_id = session.get("carro_id")
    carro = sessao.query(Veiculo).filter_by(id = carro_id).first()
    garagem = sessao.query(Garagem).filter_by(id = carro.id_garagem).first()
    status_locacao = "Confirmada"
    data_horario_pedido = datetime.now()
    formato = "%Y-%m-%dT%H:%M"  
    data_horario_entrega = datetime.strptime(session.get("horario_entrega"), formato)
    data_horario_devolucao = datetime.strptime(session.get("horario_devolucao"), formato)
    local_entrega = "Garagem "+ garagem.bairro
    local_devolucao = session.get("local_devolucao")
    try:
        comprar_carro(id_carro=carro_id,id_cliente=id_usuario, data_horario_entrega=data_horario_entrega,data_horario_devolucao=data_horario_devolucao, local_devolucao=local_devolucao,local_entrega=local_entrega, status_locacao=status_locacao, data_horario_pedido=data_horario_pedido )  
    finally:
        sessao.close()

    return redirect(url_for("pagina_inicial"))

@app.route("/contato")
def contato():
    usuario = session.get("id_usuario")
    return render_template("contato.html", usuario = usuario)
    


if __name__=="__main__":
    app.run(debug=True)


