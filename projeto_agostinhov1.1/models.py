from datetime import datetime, date
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Float, DateTime, Date, Numeric
from sqlalchemy.orm import sessionmaker, declarative_base


bd = create_engine("sqlite:///projeto_concessionaria.db")

Sessao = sessionmaker(bind = bd)




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
    cpf = Column("cpf", String(11))
    doc_identificacao = Column("doc_identificacao", String(20))
    nome = Column("nome", String(200), nullable=False)
    email = Column("email", String(255), nullable=False)
    senha = Column("senha", String(100), nullable=False)
    data_nasc = Column("data_nasc", Date, nullable=False)
    cnh = Column("cnh", String(20), nullable=False)

    def __init__(self, nome, email, senha, data_nasc, cnh, cpf, doc_identificacao):
        self.cpf = cpf
        self.doc_identificacao = doc_identificacao
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
    id_garagem = Column("id_garagem", Integer, ForeignKey("garagens.id"))

    def __init__(self, status_locacao, data_horario_pedido, data_horario_entrega, data_horario_devolucao, id_cliente, id_veiculo, local_entrega, local_devolucao, id_garagem):
        self.status_locacao = status_locacao
        self.data_horario_pedido = data_horario_pedido
        self.data_horario_entrega = data_horario_entrega
        self.local_entrega = local_entrega
        self.data_horario_devolucao = data_horario_devolucao
        self.local_devolucao = local_devolucao
        self.id_cliente = id_cliente
        self.id_veiculo = id_veiculo
        self.id_garagem = id_garagem

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
    nome_garagem = Column("nome_garagem", String(200), nullable=False)
    logradouro = Column("logradouro", String(200), nullable=False)
    endereco_numero = Column("endereco_numero", Integer)
    bairro = Column("bairro", String(200))
    cep = Column("cep", String(8))
    cidade = Column("cidade", String(200), nullable=False)
    estado = Column("estado", String(200), nullable=False)
    pais = Column("pais", String(200), nullable=False)
    capacidade = Column("capacidade", Integer, nullable=False)

    def __init__(self,nome_garagem, logradouro, cidade, estado, pais, capacidade, endereco_numero, bairro, cep):
        self.nome_garagem = nome_garagem
        self.logradouro = logradouro
        self.endereco_numero = endereco_numero
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
        self.capacidade = capacidade







Base.metadata.create_all(bind = bd)





# Inserts convertidos para SQLAlchemy - Parte 1: Clientes e Telefones
try:
    sessao = Sessao()

    # Inserts clientes brasileiros
    sessao.add_all([
        Cliente(cpf="00659599066", nome="Douglas Rocha Melo", email="douglas.melo123@gmail.com", senha="k202yY8", data_nasc=date.fromisoformat("1964-02-12"), cnh="81739983279", doc_identificacao=None),
        Cliente(cpf="01549751760", nome="Vinicius Lima Oliveira", email="vinicius.lima123@gmail.com", senha="32Q6Jl58", data_nasc=date.fromisoformat("1979-10-28"), cnh="94771495974", doc_identificacao=None),
        Cliente(cpf="80155993348", nome="Kauan Gomes Sousa", email="kauan.sousa123@gmail.com", senha="euK8h42w", data_nasc=date.fromisoformat("1991-09-16"), cnh="51163741547", doc_identificacao=None),
        Cliente(cpf="40987967673", nome="Leila Correia Oliveira", email="leila.oliveira123@gmail.com", senha="euK8h42w", data_nasc=date.fromisoformat("1990-04-06"), cnh="42409412601", doc_identificacao=None),
        Cliente(cpf="51954757255", nome="Manuela Pinto Cunha", email="manuela.cunha123@gmail.com", senha="UO0sTx97", data_nasc=date.fromisoformat("2000-11-20"), cnh="34387728373", doc_identificacao=None),
    ])

    # Inserts telefones dos clientes brasileiros
    sessao.add_all([
        TelefoneCliente(id_cliente=1, telefone="8339482363"),
        TelefoneCliente(id_cliente=2, telefone="4132882488"),
        TelefoneCliente(id_cliente=3, telefone="6724707408"),
        TelefoneCliente(id_cliente=4, telefone="5421339827"),
        TelefoneCliente(id_cliente=5, telefone="2837548842"),
    ])

    # Inserts clientes estrangeiros
    sessao.add_all([
        Cliente(cpf=None, nome="Jill A. Reeves", email="jill.reeves@gmail.com", senha="1jMkU347", data_nasc=date.fromisoformat("1992-12-24"), cnh="16596229870", doc_identificacao="X123456Y"),
        Cliente(cpf=None, nome="Allan D. Troncoso", email="allan.troncoso@gmail.com", senha="fepG1572", data_nasc=date.fromisoformat("1984-07-13"), cnh="46743128668", doc_identificacao="Z1112228C"),
    ])

    sessao.commit()
    print("Parte 1 inserida com sucesso!")
except Exception as e:
    sessao.rollback()
    print(f"Erro na Parte 1: {str(e)}")
finally:
    sessao.close()

 






# Inserts convertidos para SQLAlchemy - Parte 2: Telefones Estrangeiros, Fornecedores e Telefones Fornecedores
try:
    sessao = Sessao()

    # Inserts telefones dos clientes estrangeiros
    sessao.add_all([
        TelefoneCliente(id_cliente=6, telefone="+1 5056573563"),
        TelefoneCliente(id_cliente=7, telefone="+1 5056441586"),
    ])

    # Inserts fornecedores de veículos
    sessao.add_all([
        Fornecedor(nome="Stellantis", cidade="Betim", estado="Minas Gerais", pais="Brasil", pais_origem="Holanda", ano_fundacao=2021, logradouro="Avenida do Contorno", endereco_numero=3455, bairro="Paulo Camilo", cep="32669900", cnpj="16701716000156"),
        Fornecedor(nome="General Motors", cidade="São José dos Campos", estado="São Paulo", pais="Brasil", pais_origem="Estados Unidos", ano_fundacao=1925, logradouro="Avenida General Motors", endereco_numero=1959, bairro="Motorama", cep="12221900", cnpj="59275792000826"),
        Fornecedor(nome="Volkswagen do Brasil", cidade="São Bernardo do Campo", estado="São Paulo", pais="Brasil", pais_origem="Alemanha", ano_fundacao=1959, logradouro="Via Anchieta", endereco_numero=3600, bairro="Demarchi", cep="09823901", cnpj="59104422005704"),
        Fornecedor(nome="Toyota do Brasil", cidade="Sorocaba", estado="São Paulo", pais="Brasil", pais_origem="Japão", ano_fundacao=1937, logradouro="Avenida Toyota", endereco_numero=9005, bairro="Itavuvu", cep="18079755", cnpj="59104760000604"),
        Fornecedor(nome="Hyundai Motor Brasil", cidade="Piracicaba", estado="São Paulo", pais="Brasil", pais_origem="Coreia do Sul", ano_fundacao=1967, logradouro="Avenida Hyundai", endereco_numero=777, bairro="Água Santa", cep="13413900", cnpj="10394422000142"),
    ])

    # Inserts telefones dos fornecedores de veículos
    sessao.add_all([
        TelefoneFornecedor(id_fornecedor=1, telefone="08007270660"),
        TelefoneFornecedor(id_fornecedor=1, telefone="5595697220"),
        TelefoneFornecedor(id_fornecedor=2, telefone="08007024200"),
        TelefoneFornecedor(id_fornecedor=3, telefone="551147008838"),
        TelefoneFornecedor(id_fornecedor=4, telefone="08007030206"),
        TelefoneFornecedor(id_fornecedor=5, telefone="08007703355"),
    ])

    sessao.commit()
    print("Parte 2 inserida com sucesso!")
except Exception as e:
    sessao.rollback()
    print(f"Erro na Parte 2: {str(e)}")
finally:
    sessao.close()





 # Inserts convertidos para SQLAlchemy - Parte 3: Funcionários, Telefones Funcionários e Marcas
try:
    sessao = Sessao()

    # Inserts funcionarios da locadora (senhas fictícias criadas, pois não podem ser null)
    sessao.add_all([
        Funcionario(cpf="54494242055", nome="Joao Silva Azevedo", senha="senha123", data_nasc=date.fromisoformat("1987-04-05"), email="joao.silva@show.com", cargo="Vistoriador", salario=4200.00, data_admissao=date.fromisoformat("2010-01-30")),
        Funcionario(cpf="54131026074", nome="Antônio Gomes Barbosa", senha="senha456", data_nasc=date.fromisoformat("2000-10-16"), email="antonio.barbosa@show.com", cargo="Atendente", salario=2200.00, data_admissao=date.fromisoformat("2018-05-08")),
        Funcionario(cpf="27086430021", nome="Brenda Araujo Cardoso", senha="senha789", data_nasc=date.fromisoformat("1991-06-18"), email="brenda.cardoso@show.com", cargo="Supervisor de Vendas", salario=7200.00, data_admissao=date.fromisoformat("2015-03-22")),
        Funcionario(cpf="99921688030", nome="Isabelle Santos Rodrigues", senha="senha101", data_nasc=date.fromisoformat("1994-07-29"), email="isabelle.santos@show.com", cargo="Mecânico", salario=2800.00, data_admissao=date.fromisoformat("2017-06-13")),
        Funcionario(cpf="36018794098", nome="Julia Santos Ribeiro", senha="senha112", data_nasc=date.fromisoformat("1979-11-10"), email="julia.ribeiro@show.com", cargo="Analista de dados", salario=9000.00, data_admissao=date.fromisoformat("2009-05-25")),
    ])

    # Inserts telefones dos funcionarios da locadora
    sessao.add_all([
        TelefoneFuncionario(id_funcionario=1, telefone="82992834105"),
        TelefoneFuncionario(id_funcionario=2, telefone="17983757557"),
        TelefoneFuncionario(id_funcionario=3, telefone="83971661539"),
        TelefoneFuncionario(id_funcionario=4, telefone="68974536927"),
        TelefoneFuncionario(id_funcionario=5, telefone="53995347226"),
    ])

    # Inserts marcas de carros
    sessao.add_all([
        Marca(nome="Fiat", descricao="Marca italiana pertencente ao grupo Stellantis. Conhecida pela Fiat Strada e Argo."),
        Marca(nome="Chevrolet", descricao="Marca americana pertencente à General Motors. Oferece modelos como o Onix e o Camaro."),
        Marca(nome="Volkswagen", descricao="Marca alemã com forte presença no Brasil. Produz hatchbacks, sedãs, SUVs e picapes"),
        Marca(nome="Toyota", descricao="Marca japonesa conhecida por confiabilidade. Exemplo de veículo produzidos sedans, SUVs, picapes, modelos híbridos e elétricos. "),
        Marca(nome="Hyundai", descricao="Marca coreana com tecnologia avançada. Fabricante de modelos como o HB20 e o Creta."),
    ])

    sessao.commit()
    print("Parte 3 inserida com sucesso!")
except Exception as e:
    sessao.rollback()
    print(f"Erro na Parte 3: {str(e)}")
finally:
    sessao.close()




# 1. Modelo (Modelos de carros)
modelos_carros = [
    Modelo(nome="Uno", descricao="Carro compacto, econômico e versátil"),
    Modelo(nome="Onix", descricao="Carro hatch compacto com opções de motores 1.0 aspirado e 1.0 turbo"),
    Modelo(nome="SUV", descricao="Veículos com maior altura do solo, frequentemente com tração nas quatro rodas, usado normalmente em off-road."),
    Modelo(nome="Picape", descricao="Veículo com caçamba aberta na parte traseira, ideal para transporte de carga"),
    Modelo(nome="HB20", descricao="Hatchback, compacto, versátil, com porta-malas integrado à cabine")
]

# 2. Categoria (Categorias/Grupos de carros)
categorias_carros = [
    Categoria(nome="Econômico", descricao="Carros compactos e econômicos"),
    Categoria(nome="Intermediário", descricao="Carros com mais conforto e espaço em comparação aos compactos"),
    Categoria(nome="Compacto", descricao="Veículos menores e mais ágeis"),
    Categoria(nome="Adaptado", descricao="Veículos adaptado ao uso de pessoas pcd")
]

# 3. Combustivel (Tipos de combustível)
tipos_combustivel = [
    Combustivel(tipo="Gasolina"),
    Combustivel(tipo="Etanol"),
    Combustivel(tipo="Flex"),
    Combustivel(tipo="Diesel"),
    Combustivel(tipo="Elétrico")
]

# 4. Garagem (Garagens)
garagens = [
    Garagem(nome_garagem="Garagem Savassi, Belo Horizonte",logradouro="Rua das Flores", endereco_numero=123, bairro="Savassi", cep="30123456", cidade="Belo Horizonte", estado="Minas Gerais", pais="Brasil", capacidade=60),
    Garagem(nome_garagem="Garagem Cerqueira César, São Paulo",logradouro="Avenida Paulista", endereco_numero=1000, bairro="Cerqueira César", cep="01310900", cidade="São Paulo", estado="São Paulo", pais="Brasil", capacidade=100),
    Garagem(nome_garagem="Garagem Botafogo, Rio de Janeiro",logradouro="Praia de Botafogo", endereco_numero=500, bairro="Botafogo", cep="22250900", cidade="Rio de Janeiro", estado="Rio de Janeiro", pais="Brasil", capacidade=60),
    Garagem(nome_garagem="Garagem Meireles, Fortaleza",logradouro="Avenida Beira Mar", endereco_numero=200, bairro="Meireles", cep="60165040", cidade="Fortaleza", estado="Ceará", pais="Brasil", capacidade=50),
    Garagem(nome_garagem="Garagem Centro, Porto Alegre",logradouro="Rua da Praia", endereco_numero=55, bairro="Centro", cep="90010030", cidade="Porto Alegre", estado="Rio Grande do Sul", pais="Brasil", capacidade=80)
]

# 5. PlanoSeguro (Planos de seguro)
planos_seguro = [
    PlanoSeguro(tipo="Essencial", descricao="Proteção contra furto, incêndio e danos por colisões", preco=35.00),
    PlanoSeguro(tipo="Intermediario", descricao="Pacote essencial, proteção contra terceiros e redução de coparticipação", preco=50.00),
    PlanoSeguro(tipo="Completa", descricao="Pacote intermediario, isenção total de coparticipação e proteção contra danos a vidros e pneus", preco=80.00)
]

# 6. ItemAdicional (Itens adicionais)
itens_adicionais = [
    ItemAdicional(nome="Bebê Conforto", preco=30.00, descricao="Assento para crianças de 0 a 1 anos, uso obrigatório"),
    ItemAdicional(nome="Cadeirinha", preco=30.00, descricao="Assento para crianças de 1 a 4 anos, uso obrigatório"),
    ItemAdicional(nome="Assento de Elevação", preco=30.00, descricao="Assento para crianças de 4 a 7 anos ou que não atingiram altura minima (1,45 m)"),
    ItemAdicional(nome="Lavagem Antecipada", preco=80.00, descricao="Veículo não precisa vir limpo na devolução")
]

# 7. Veiculo (Veículos)
# NOTA: Os IDs (idFornecedor, idGaragem, etc.) devem ser preenchidos com os valores corretos após a inserção dos dados nas tabelas relacionadas.
# Assumindo que os IDs estão na ordem de 1 a N de acordo com os inserts anteriores:
veiculos = [
    Veiculo(portas=4, preco_diaria=100.00, placa="ABC1D23", cor="Prata", preco_compra=80000.00, capacidade_pessoas=5, quilometragem=15000, cambio="Manual", airbags=True, ar_condicionado=True, disponivel=True, id_fornecedor=1, id_garagem=1, id_plano_seguro=1, id_marca=1, id_modelo=1, id_categoria=1, id_combustivel=3),
    Veiculo(portas=4, preco_diaria=150.00, placa="EFG2H45", cor="Branco", preco_compra=75000.00, capacidade_pessoas=5, quilometragem=8000, cambio="Automático", airbags=True, ar_condicionado=True, disponivel=True, id_fornecedor=2, id_garagem=2, id_plano_seguro=2, id_marca=2, id_modelo=2, id_categoria=2, id_combustivel=1),
    Veiculo(portas=4, preco_diaria=180.00, placa="IJK3L67", cor="Preto", preco_compra=80000.00, capacidade_pessoas=5, quilometragem=20000, cambio="Automático", airbags=True, ar_condicionado=True, disponivel=True, id_fornecedor=3, id_garagem=3, id_plano_seguro=2, id_marca=3, id_modelo=3, id_categoria=2, id_combustivel=3),
    Veiculo(portas=4, preco_diaria=300.00, placa="MNO4P89", cor="Cinza", preco_compra=120000.00, capacidade_pessoas=5, quilometragem=5000, cambio="Automático", airbags=True, ar_condicionado=True, disponivel=True, id_fornecedor=4, id_garagem=4, id_plano_seguro=3, id_marca=4, id_modelo=4, id_categoria=2, id_combustivel=4),
    Veiculo(portas=4, preco_diaria=200.00, placa="QRS5T01", cor="Vermelho", preco_compra=100000.00, capacidade_pessoas=5, quilometragem=12000, cambio="Automático", airbags=True, ar_condicionado=True, disponivel=True, id_fornecedor=5, id_garagem=5, id_plano_seguro=3, id_marca=5, id_modelo=5, id_categoria=4, id_combustivel=2),
    Veiculo(portas=2, preco_diaria=200.00, placa="UVW5X01", cor="Preto", preco_compra=90000.00, capacidade_pessoas=5, quilometragem=12000, cambio="Automático", airbags=False, ar_condicionado=True, disponivel=True, id_fornecedor=5, id_garagem=5, id_plano_seguro=3, id_marca=5, id_modelo=5, id_categoria=4, id_combustivel=2)
]

# 8. Locacao (Locações)
locacoes = [
    Locacao(status_locacao="Concluída", data_horario_pedido=datetime(2024, 1, 15, 10, 2, 1), data_horario_entrega=datetime(2024, 1, 20, 14, 0, 0), local_entrega="Garagem Centro, Porto Alegre", data_horario_devolucao=datetime(2024, 1, 30, 10, 0, 0), local_devolucao="Garagem Centro, Porto Alegre", id_cliente=1, id_veiculo=1, id_garagem=5),
    Locacao(status_locacao="Concluída", data_horario_pedido=datetime(2023, 2, 21, 20, 40, 11), data_horario_entrega=datetime(2023, 3, 1, 14, 0, 0), local_entrega="Garagem Centro, Porto Alegre", data_horario_devolucao=datetime(2023, 3, 20, 14, 0, 0), local_devolucao="Garagem Centro, Porto Alegre", id_cliente=1, id_veiculo=4, id_garagem=5),
    Locacao(status_locacao="Em Andamento", data_horario_pedido=datetime(2025, 11, 1, 13, 42, 21), data_horario_entrega=datetime(2025, 11, 10, 11, 0, 0), local_entrega="Garagem Centro, Porto Alegre", data_horario_devolucao=datetime(2025, 11, 25, 18, 0, 0), local_devolucao="Garagem Centro, Porto Alegre", id_cliente=2, id_veiculo=2, id_garagem=5),
    Locacao(status_locacao="Pendente", data_horario_pedido=datetime(2025, 12, 1, 22, 13, 14), data_horario_entrega=datetime(2025, 12, 6, 12, 0, 0), local_entrega="Garagem Centro, Porto Alegre", data_horario_devolucao=datetime(2025, 12, 30, 16, 0, 0), local_devolucao="Garagem Centro, Porto Alegre", id_cliente=3, id_veiculo=3, id_garagem=5),
    Locacao(status_locacao="Concluída", data_horario_pedido=datetime(2022, 6, 15, 11, 0, 0), data_horario_entrega=datetime(2022, 6, 21, 13, 0, 0), local_entrega="Garagem Botafogo, Rio de Janeiro", data_horario_devolucao=datetime(2022, 6, 29, 10, 0, 0), local_devolucao="Garagem Botafogo, Rio de Janeiro", id_cliente=5, id_veiculo=5, id_garagem=3),
    # Locação cancelada
    Locacao(status_locacao="Cancelada", data_horario_pedido=datetime(2021, 2, 7, 19, 41, 54), data_horario_entrega=datetime(2021, 2, 22, 9, 0, 0), local_entrega=None, data_horario_devolucao=datetime(2024, 2, 2, 16, 0, 0), local_devolucao=None, id_cliente=4, id_veiculo=4, id_garagem=None)
]

# 9. Gerencia (Relação Funcionario-Locação)
gerencias = [
    Gerencia(id_funcionario=1, id_locacao=1),
    Gerencia(id_funcionario=1, id_locacao=2),
    Gerencia(id_funcionario=3, id_locacao=3),
    Gerencia(id_funcionario=5, id_locacao=4),
    Gerencia(id_funcionario=4, id_locacao=5)
]

# 10. Inclui (Relação Locação-ItemAdicional)
incluis = [
    Inclui(id_locacao=1, id_item_adicional=1),
    Inclui(id_locacao=1, id_item_adicional=2),
    Inclui(id_locacao=2, id_item_adicional=3),
    Inclui(id_locacao=4, id_item_adicional=2),
    Inclui(id_locacao=5, id_item_adicional=1)
]

# 11. Avaliacao (Avaliações)
avaliacoes = [
    Avaliacao(data_horario_avaliacao=datetime(2024, 1, 30, 20, 43, 12), nota=10, texto="Carro excelente e atendimento perfeito!", id_cliente=1, id_veiculo=1),
    Avaliacao(data_horario_avaliacao=datetime(2025, 11, 26, 15, 38, 9), nota=8, texto="Bom carro, mas poderia ser mais econômico :(", id_cliente=2, id_veiculo=2),
    Avaliacao(data_horario_avaliacao=datetime(2024, 1, 26, 9, 45, 27), nota=3, texto="Muito caro, pouco confortavel no banco traseiro e fui zuado por ser 'carro de mulher'", id_cliente=2, id_veiculo=3),
    Avaliacao(data_horario_avaliacao=datetime(2022, 7, 1, 14, 20, 39), nota=7, texto="Carro bonito com alguns detalhes a melhorar na parte mecânica", id_cliente=4, id_veiculo=5),
    Avaliacao(data_horario_avaliacao=datetime(2024, 1, 30, 16, 10, 0), nota=10, texto="Veículo adaptado funcionou muito bem. Fofo", id_cliente=4, id_veiculo=4)
]

# 12. Pagamento (Pagamentos)
pagamentos = [
    Pagamento(valor=600.00, data_horario_pagamento=datetime(2024, 1, 28, 10, 30, 22), metodo="Cartão de Crédito", id_locacao=1),
    Pagamento(valor=750.00, data_horario_pagamento=datetime(2025, 11, 26, 9, 30, 12), metodo="PIX", id_locacao=2),
    Pagamento(valor=900.00, data_horario_pagamento=datetime(2024, 1, 25, 8, 30, 36), metodo="Cartão de Débito", id_locacao=3),
    Pagamento(valor=1500.00, data_horario_pagamento=datetime(2024, 1, 28, 16, 30, 50), metodo="Cartão de Crédito", id_locacao=4),
    Pagamento(valor=1000.00, data_horario_pagamento=datetime(2024, 1, 10, 11, 30, 48), metodo="Pix", id_locacao=5)
]
session = Sessao()
try:
     # Inserir as tabelas base
     session.add_all(modelos_carros)
     session.add_all(categorias_carros)
     session.add_all(tipos_combustivel)
     session.add_all(garagens)
     session.add_all(planos_seguro)
     session.add_all(itens_adicionais)
   
     # Inserir veículos (dependem das tabelas base)
     session.add_all(veiculos)
   
     # Inserir locações (dependem de Cliente e Veículo)
     session.add_all(locacoes)
   
     # Inserir as tabelas de relacionamento e outras (dependem de Locação, Cliente, Veículo)
     session.add_all(gerencias)
     session.add_all(incluis)
     session.add_all(avaliacoes)
     session.add_all(pagamentos)
     session.commit()
     print("Todos os inserts foram realizados com sucesso!")
except Exception as e:
     session.rollback()
     print(f"Ocorreu um erro: {e}")
finally:
     session.close()




try:
    gabriel=Funcionario(cpf="45715291801", nome="admin", senha="123", data_nasc=date.fromisoformat("1930-04-05"), email="gabriel@gmail.com", cargo="administrador", salario=9999.99, data_admissao=date.fromisoformat("2000-04-05"))
    sessao = Sessao()
    sessao.add(gabriel)
    sessao.commit()
    sessao.close()
except Exception as e:
    print(e)





# Funções 


def cadastrar_cliente(nome, email, senha, data_nasc, cnh,cpf, doc_identificacao, telefone):
    sessao = Sessao()
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
        # Conversões
        portas = int(portas)
        preco_diaria = float(preco_diaria)
        preco_compra = float(preco_compra)
        capacidade_pessoas = int(capacidade_pessoas)
        quilometragem = int(quilometragem)
        sessao =Sessao()
        print(f"Cadastrando carro: portas={portas}, preco_diaria={preco_diaria}, ...")  
        fornecedor_obj = sessao.query(Fornecedor).filter_by(nome=fornecedor).first()
        if not fornecedor_obj:
            return "Erro: Fornecedor não encontrado"
        id_fornecedor = fornecedor_obj.id
        
        garagem_obj = sessao.query(Garagem).filter_by(cep=garagem).first()
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
    

    
