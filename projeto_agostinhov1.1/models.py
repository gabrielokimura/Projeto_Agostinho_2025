from datetime import datetime, date
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Float, DateTime, Date, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base


bd = create_engine("sqlite:///projeto_concessionaria.db")

Sessao = sessionmaker(bind = bd)

sessao = Sessao()


Base = declarative_base()


class Avaliacao(Base):
    __tablename__ = "avaliacoes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    data_horario_avaliacao = Column("data_horario_avaliacao", DateTime, nullable=False)
    nota = Column("nota", Integer)
    texto = Column("texto", String(255))
    id_cliente = Column("id_cliente", Integer, ForeignKey("clientes.id"), nullable=False)
    id_veiculo = Column("id_veiculo", Integer, ForeignKey("veiculos.id"), nullable=False)

    def __init__(self, data_horario_avaliacao, id_cliente, id_veiculo, nota, texto):
        self.data_horario_avaliacao = data_horario_avaliacao
        self.nota = nota
        self.texto = texto
        self.id_cliente = id_cliente
        self.id_veiculo = id_veiculo



class Cliente(Base):
    __tablename__ = "clientes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    cpf = Column("cpf", String(11), nullable=False)
    doc_identificacao = Column("doc_identificacao", String(20))
    nome = Column("nome", String(200), nullable=False)
    email = Column("email", String(255), nullable=False)
    senha = Column("senha", String(100), nullable=False)
    data_nasc = Column("data_nasc", Date, nullable=False)
    cnh = Column("cnh", String(20), nullable=False)

    def __init__(self, nome, email, senha, data_nasc, cnh, cpf, doc_identificacao):
        self.cpf = cpf
        self.documento_identificacao = doc_identificacao
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nasc = data_nasc
        self.cnh = cnh



    





class TelefoneCliente(Base):
    __tablename__ = "telefone_clientes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_cliente = Column("id_cliente", Integer, ForeignKey("clientes.id"), nullable=False)
    telefone = Column("telefone", String(20))

    def __init__(self, id_cliente, telefone):
        self.id_cliente = id_cliente
        self.telefone = telefone




class Fornecedor(Base):
    __tablename__ = "fornecedores"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(200), nullable=False)
    ano_fundacao = Column("ano_fundacao", Integer)
    pais_origem = Column("pais_origem", String(200))
    cidade = Column("cidade", String(255))
    estado = Column("estado", String(255), nullable=False)
    pais = Column("pais", String(255), nullable=False)
    logradouro = Column("logradouro", String(255))
    endereco_numero = Column("endereco_numero", Integer)
    bairro = Column("bairro", String(200))
    cep = Column("cep", String(8))
    cnpj = Column("cnpj", String(14), nullable=False)

    def __init__(self, nome, estado, pais, cnpj, ano_fundacao, pais_origem, cidade, logradouro, endereco_numero, bairro, cep):
        self.nome = nome
        self.ano_fundacao = ano_fundacao
        self.pais_origem = pais_origem
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.logradouro = logradouro
        self.endereco_numero = endereco_numero
        self.bairro = bairro
        self.cep = cep
        self.cnpj = cnpj



class TelefoneFornecedor(Base):
    __tablename__ = "telefone_fornecedores"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_fornecedor = Column("id_fornecedor", Integer, ForeignKey("fornecedores.id"), nullable=False)
    telefone = Column("telefone", String(20))

    def __init__(self, id_fornecedor, telefone):
        self.id_fornecedor = id_fornecedor
        self.telefone = telefone



class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    cpf = Column("cpf", String(11), nullable=False)
    nome = Column("nome", String(200), nullable=False)
    senha = Column("senha", String(200), nullable=False)
    data_nasc = Column("data_nasc", Date, nullable=False)
    email = Column("email", String(255), nullable=False)
    cargo = Column("cargo", String(255), nullable=False)
    salario = Column("salario", Numeric(10, 2), nullable=False)
    data_admissao = Column("data_admissao", Date, nullable=False)

    def __init__(self, cpf, nome,senha, data_nasc, email, cargo, salario, data_admissao):
        self.cpf = cpf
        self.nome = nome
        self.senha=senha
        self.data_nasc = data_nasc
        self.email = email
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao




class TelefoneFuncionario(Base):
    __tablename__ = "telefone_funcionarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_funcionario = Column("id_funcionario", Integer, ForeignKey("funcionarios.id"), nullable=False)
    telefone = Column("telefone", String(20))

    def __init__(self, id_funcionario, telefone):
        self.id_funcionario = id_funcionario
        self.telefone = telefone



class Locacao(Base):
    __tablename__ = "locacoes"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status_locacao = Column("status_locacao", String(100), nullable=False)
    data_horario_pedido = Column("data_horario_pedido", DateTime, nullable=False)
    data_horario_entrega = Column("data_horario_entrega", DateTime, nullable=False)
    local_entrega = Column("local_entrega", String(255))
    data_horario_devolucao = Column("data_horario_devolucao", DateTime, nullable=False)
    local_devolucao = Column("local_devolucao", String(255))
    id_cliente = Column("id_cliente", Integer, ForeignKey("clientes.id"), nullable=False)
    id_veiculo = Column("id_veiculo", Integer, ForeignKey("veiculos.id"), nullable=False)

    def __init__(self, status_locacao, data_horario_pedido, data_horario_entrega, data_horario_devolucao, id_cliente, id_veiculo, local_entrega, local_devolucao):
        self.status_locacao = status_locacao
        self.data_horario_pedido = data_horario_pedido
        self.data_horario_entrega = data_horario_entrega
        self.local_entrega = local_entrega
        self.data_horario_devolucao = data_horario_devolucao
        self.local_devolucao = local_devolucao
        self.id_cliente = id_cliente
        self.id_veiculo = id_veiculo

# Tabela: Gerencia (junção de tabela)
class Gerencia(Base):
    __tablename__ = "gerencias"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_funcionario = Column("id_funcionario", Integer, ForeignKey("funcionarios.id"), nullable=False)
    id_locacao = Column("id_locacao", Integer, ForeignKey("locacoes.id"), nullable=False)

    def __init__(self, id_funcionario, id_locacao):
        self.id_funcionario = id_funcionario
        self.id_locacao = id_locacao




class ItemAdicional(Base):
    __tablename__ = "item_adicionais"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(100), nullable=False)
    preco = Column("preco", Numeric(10, 2), nullable=False)
    descricao = Column("descricao", String(200), nullable=False)

    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

# Tabela Inclui (junção de tabela)
class Inclui(Base):
    __tablename__ = "incluis"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_locacao = Column("id_locacao", Integer, ForeignKey("locacoes.id"), nullable=False)
    id_item_adicional = Column("id_item_adicional", Integer, ForeignKey("item_adicionais.id"), nullable=False)

    def __init__(self, id_locacao, id_item_adicional):
        self.id_locacao = id_locacao
        self.id_item_adicional = id_item_adicional




class Pagamento(Base):
    __tablename__ = "pagamentos"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    valor = Column("valor", Numeric(10, 2), nullable=False)
    data_horario_pagamento = Column("data_horario_pagamento", DateTime, nullable=False)
    metodo = Column("metodo", String(100), nullable=False)
    id_locacao = Column("id_locacao", Integer, ForeignKey("locacoes.id"), nullable=False)

    def __init__(self, valor, data_horario_pagamento, metodo, id_locacao):
        self.valor = valor
        self.data_horario_pagamento = data_horario_pagamento
        self.metodo = metodo
        self.id_locacao = id_locacao





class PlanoSeguro(Base):
    __tablename__ = "plano_seguros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    tipo = Column("tipo", String(100), nullable=False)
    descricao = Column("descricao", String(100), nullable=False)
    preco = Column("preco", Numeric(10, 2), nullable=False)

    def __init__(self, tipo, descricao, preco):
        self.tipo = tipo
        self.descricao = descricao
        self.preco = preco




class Veiculo(Base):
    __tablename__ = "veiculos"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    portas = Column("portas", Integer, nullable=False)
    preco_diaria = Column("preco_diaria", Numeric(10, 2), nullable=False)
    placa = Column("placa", String(7), nullable=False)
    cor = Column("cor", String(100), nullable=False)
    preco_compra = Column("preco_compra", Numeric(10, 2), nullable=False)
    capacidade_pessoas = Column("capacidade_pessoas", Integer, nullable=False)
    quilometragem = Column("quilometragem", Integer, nullable=False)
    cambio = Column("cambio", String(100), nullable=False)
    airbags = Column("airbags", Boolean, nullable=False)
    ar_condicionado = Column("ar_condicionado", Boolean, nullable=False)
    disponivel = Column("disponivel", Boolean, nullable=False)
    id_fornecedor = Column("id_fornecedor", Integer, ForeignKey("fornecedores.id"), nullable=False)
    id_garagem = Column("id_garagem", Integer, ForeignKey("garagens.id"), nullable=False)
    id_plano_seguro = Column("id_plano_seguro", Integer, ForeignKey("plano_seguros.id"), nullable=False)
    id_marca = Column("id_marca", Integer, ForeignKey("marcas.id"), nullable=False)
    id_modelo = Column("id_modelo", Integer, ForeignKey("modelos.id"), nullable=False)
    id_categoria = Column("id_categoria", Integer, ForeignKey("categorias.id"), nullable=False)
    id_combustivel = Column("id_combustivel", Integer, ForeignKey("combustiveis.id"), nullable=False)

    def __init__(self, portas, preco_diaria, placa, cor, preco_compra, capacidade_pessoas, quilometragem, cambio, airbags, ar_condicionado, disponivel, id_fornecedor, id_garagem, id_plano_seguro, id_marca, id_modelo, id_categoria, id_combustivel):
        self.portas = portas
        self.preco_diaria = preco_diaria
        self.placa = placa
        self.cor = cor
        self.preco_compra = preco_compra
        self.capacidade_pessoas = capacidade_pessoas
        self.quilometragem = quilometragem
        self.cambio = cambio
        self.airbags = airbags
        self.ar_condicionado = ar_condicionado
        self.disponivel = disponivel
        self.id_fornecedor = id_fornecedor
        self.id_garagem = id_garagem
        self.id_plano_seguro = id_plano_seguro
        self.id_marca = id_marca
        self.id_modelo = id_modelo
        self.id_categoria = id_categoria
        self.id_combustivel = id_combustivel




class Combustivel(Base):
    __tablename__ = "combustiveis"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    tipo = Column("tipo", String(50), nullable=False, unique=True)

    def __init__(self, tipo):
        self.tipo = tipo




class Modelo(Base):
    __tablename__ = "modelos"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(255), nullable=False)
    descricao = Column("descricao", String(255))

    def __init__(self, nome, descricao=None):
        self.nome = nome
        self.descricao = descricao




class Marca(Base):
    __tablename__ = "marcas"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(255), nullable=False)
    descricao = Column("descricao", String(255))

    def __init__(self, nome, descricao=None):
        self.nome = nome
        self.descricao = descricao




class Categoria(Base):
    __tablename__ = "categorias"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String(255), nullable=False)
    descricao = Column("descricao", String(255))

    def __init__(self, nome, descricao=None):
        self.nome = nome
        self.descricao = descricao





class Garagem(Base):
    __tablename__ = "garagens"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    logradouro = Column("logradouro", String(200), nullable=False)
    endereco_numero = Column("endereco_numero", Integer)
    bairro = Column("bairro", String(200))
    cep = Column("cep", String(8))
    cidade = Column("cidade", String(200), nullable=False)
    estado = Column("estado", String(200), nullable=False)
    pais = Column("pais", String(200), nullable=False)
    capacidade = Column("capacidade", Integer, nullable=False)

    def __init__(self, logradouro, cidade, estado, pais, capacidade, endereco_numero, bairro, cep):
        self.logradouro = logradouro
        self.endereco_numero = endereco_numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.capacidade = capacidade







Base.metadata.create_all(bind = bd)







# Funções 


def cadastrar_cliente(nome, senha, email, telefone, data_nasc, cpf,cnh, doc_identificacao):
    data_nasc2 = date.fromisoformat(data_nasc)
    novo_cliente = Cliente(nome,email, senha, data_nasc2, cnh, cpf, doc_identificacao)
    sessao.add(novo_cliente)
    sessao.commit()

    if telefone:
        novo_telefone = TelefoneCliente(novo_cliente.id, telefone)
        sessao.add(novo_telefone)
    sessao.commit()
    sessao.close()



""" portas, preco_diaria, placa, cor, preco_compra, capacidade_pessoas,quilometragem, cambio,airbags,ar_condicionado,disponivel,id_fornecedor,id_garage,id_plano_seguro,id_marca,id_modelo,id_categoria,id_combustivel """



def cadastrar_carro(portas, preco_diaria, placa, cor, preco_compra, capacidade_pessoas, quilometragem, cambio, airbags, ar_condicionado, disponivel, fornecedor, garagem, plano_seguro, marca, modelo, categoria, combustivel):
    try:
        print(f"Cadastrando carro: portas={portas}, preco_diaria={preco_diaria}, ...")  # Log
        fornecedor_obj = sessao.query(Fornecedor).filter_by(nome=fornecedor).first()
        if not fornecedor_obj:
            return "Erro: Fornecedor não encontrado"
        id_fornecedor = fornecedor_obj.id
        
        garagem_obj = sessao.query(Garagem).filter_by(bairro=garagem).first()
        if not garagem_obj:
            return "Erro: Garagem não encontrada"
        id_garagem = garagem_obj.id
        
        plano_seguro_obj = sessao.query(PlanoSeguro).filter_by(tipo=plano_seguro).first()
        if not plano_seguro_obj:
            return "Erro: Plano seguro não encontrado"
        id_plano_seguro = plano_seguro_obj.id
        
        marca_obj = sessao.query(Marca).filter_by(nome=marca).first()
        if not marca_obj:
            return "Erro: Marca não encontrada"
        id_marca = marca_obj.id
        
        modelo_obj = sessao.query(Modelo).filter_by(nome=modelo).first()
        if not modelo_obj:
            return "Erro: Modelo não encontrado"
        id_modelo = modelo_obj.id
        
        categoria_obj = sessao.query(Categoria).filter_by(nome=categoria).first()
        if not categoria_obj:
            return "Erro: Categoria não encontrada"
        id_categoria = categoria_obj.id
        
        combustivel_obj = sessao.query(Combustivel).filter_by(tipo=combustivel).first()
        if not combustivel_obj:
            return "Erro: Combustível não encontrado"
        id_combustivel = combustivel_obj.id
        
        novo_carro = Veiculo(
            portas=portas, preco_diaria=preco_diaria, placa=placa, cor=cor, preco_compra=preco_compra,
            capacidade_pessoas=capacidade_pessoas, quilometragem=quilometragem, cambio=cambio, airbags=airbags,
            ar_condicionado=ar_condicionado, disponivel=disponivel, id_fornecedor=id_fornecedor,
            id_garagem=id_garagem, id_plano_seguro=id_plano_seguro, id_marca=id_marca, id_modelo=id_modelo,
            id_categoria=id_categoria, id_combustivel=id_combustivel
        )
        sessao.add(novo_carro)
        sessao.commit()
        return "Carro cadastrado com sucesso"
    except Exception as e:
        sessao.rollback()
        return f"Erro: {str(e)}"
    finally:
        sessao.close()
