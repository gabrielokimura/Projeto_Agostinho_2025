

class Modelo:
    carros_cadastrados = []
    usuarios_cadastrados=[{"nome":"Admin123", "senha":"123", "admin":True}]



    

    


    def cadastrar_carro(self,carro):
        self.carros_cadastrados.append(carro)



    def achar_carro(self, id):
        carro_encontrado = None
        for carro in self.carros_cadastrados:
            if carro["id"] == id:
                carro_encontrado = carro
                return carro_encontrado
        if carro_encontrado is None:
            return None
        







""" 

kiki = Funcionario("11111111111","admin","123",date(2000, 6, 17), "admin@gmail.com", "administrador", 9999.99, date(2025, 11, 1))
sessao.add(kiki)
sessao.commit()
 """

""" try:
    # Marcas
    sessao.add(Marca(nome="Marca_1", descricao="Marca de exemplo 1"))
    sessao.add(Marca(nome="Marca_2", descricao="Marca de exemplo 2"))
    sessao.add(Marca(nome="Marca_3", descricao="Marca de exemplo 3"))
    sessao.add(Marca(nome="Marca_4", descricao="Marca de exemplo 4"))
    sessao.add(Marca(nome="Marca_5", descricao="Marca de exemplo 5"))
    # Modelos
    sessao.add(Modelo(nome="Modelo_1", descricao="Modelo básico"))
    sessao.add(Modelo(nome="Modelo_2", descricao="Modelo esportivo"))
    sessao.add(Modelo(nome="Modelo_3", descricao="Modelo luxo"))
    sessao.add(Modelo(nome="Modelo_4", descricao="Modelo econômico"))
    sessao.add(Modelo(nome="Modelo_5", descricao="Modelo compacto"))
    # Categorias
    sessao.add(Categoria(nome="Luxo", descricao="Veículos de luxo"))
    sessao.add(Categoria(nome="Econômica", descricao="Veículos econômicos"))
    sessao.add(Categoria(nome="Esportiva", descricao="Veículos esportivos"))
    # Combustíveis
    sessao.add(Combustivel(tipo="Gasolina"))
    sessao.add(Combustivel(tipo="Etanol"))
    sessao.add(Combustivel(tipo="Diesel"))
    sessao.add(Combustivel(tipo="GNV"))
     # Planos de Seguro
    sessao.add(PlanoSeguro(tipo="Cobertura_total", descricao="Cobertura completa", preco=150.00))
    sessao.add(PlanoSeguro(tipo="Cobertura_parcial", descricao="Cobertura parcial", preco=100.00))
    sessao.add(PlanoSeguro(tipo="Sem_cobertura", descricao="Sem cobertura", preco=0.00))
    # Fornecedores
    sessao.add(Fornecedor(nome="Fornecedor_1", estado="SP", pais="Brasil", cnpj="12345678000123", ano_fundacao=2000, pais_origem="Brasil", cidade="São Paulo", logradouro="Rua A, 100", endereco_numero=100, bairro="Centro", cep="01000000"))
    sessao.add(Fornecedor(nome="Fornecedor_2", estado="RJ", pais="Brasil", cnpj="98765432000198", ano_fundacao=2010, pais_origem="Brasil", cidade="Rio de Janeiro", logradouro="Av. B, 200", endereco_numero=200, bairro="Copacabana", cep="22000000"))
    sessao.add(Fornecedor(nome="Fornecedor_3", estado="MG", pais="Brasil", cnpj="45678912000145", ano_fundacao=1995, pais_origem="Brasil", cidade="Belo Horizonte", logradouro="Rua C, 300", endereco_numero=300, bairro="Savassi", cep="30100000"))
    sessao.add(Fornecedor(nome="Fornecedor_4", estado="RS", pais="Brasil", cnpj="32165498000132", ano_fundacao=2005, pais_origem="Brasil", cidade="Porto Alegre", logradouro="Av. D, 400", endereco_numero=400, bairro="Centro", cep="90000000"))
    sessao.add(Fornecedor(nome="Fornecedor_5", estado="PR", pais="Brasil", cnpj="65432178000165", ano_fundacao=2015, pais_origem="Brasil", cidade="Curitiba", logradouro="Rua E, 500", endereco_numero=500, bairro="Batel", cep="80000000"))
    # Garagens (usando bairro como identificador no select)
    sessao.add(Garagem(logradouro="Rua X, 10", cidade="São Paulo", estado="SP", pais="Brasil", capacidade=50, endereco_numero=10, bairro="Garagem_1", cep="01100000"))
    sessao.add(Garagem(logradouro="Av. Y, 20", cidade="Rio de Janeiro", estado="RJ", pais="Brasil", capacidade=40, endereco_numero=20, bairro="Garagem_2", cep="22100000"))
    sessao.add(Garagem(logradouro="Rua Z, 30", cidade="Belo Horizonte", estado="MG", pais="Brasil", capacidade=30, endereco_numero=30, bairro="Garagem_3", cep="30200000"))
    sessao.add(Garagem(logradouro="Av. W, 40", cidade="Porto Alegre", estado="RS", pais="Brasil", capacidade=60, endereco_numero=40, bairro="Garagem_4", cep="90100000"))
    sessao.add(Garagem(logradouro="Rua V, 50", cidade="Curitiba", estado="PR", pais="Brasil", capacidade=25, endereco_numero=50, bairro="Garagem_5", cep="80100000"))
    sessao.commit()
    print("Dados de exemplo inseridos com sucesso!")
except Exception as e:
    sessao.rollback()
    print(f"Erro ao inserir dados: {e}")
finally:
    sessao.close() """












""" 
const formulario = document.getElementById("formulario")
const marca = document.getElementById("marca")
const placa = document.getElementById("placa")
const disponivel = document.getElementById("disponivel")
const plano_seguro = document.getElementById("plano_seguro")
const capacidade_pessoas = document.getElementById("capacidade_pessoas")
const preco_compra = document.getElementById("preco_compra")
const fornecedor = document.getElementById("fornecedor")
const garagem = document.getElementById("garagem")
const modelo = document.getElementById("modelo")
const aluguel = document.getElementById("aluguel")
const cor = document.getElementById("cor")
const cambio = document.getElementById("cambio")
const portas = document.getElementById("portas")
const airbag = document.getElementById("airbag")
const ar_condicionado = document.getElementById("ar_condicionado")
const combustivel = document.getElementById("combustivel")
const quilometragem = document.getElementById("quilometragem")
const categoria = document.getElementById("categoria")
const CAMPOS = [marca, modelo, aluguel, cor, cambio, portas, airbag, ar_condicionado,combustivel, quilometragem, categoria]
const conteudo = document.getElementById("carros_cadastrados")
var id_carro = 0


document.addEventListener("DOMContentLoaded", carregarCarros)


formulario.addEventListener("submit", (event) =>{
    event.preventDefault()

    checarcampos()
    validarFormulario()


    
})


function checarcampos(){
    for (let campo of CAMPOS){
    const valor = campo.value
    if (valor == ""){
        erroInput(campo, "O campo "+campo.id+" é obrigatório")
    } else {
        const ItemFormulario = campo.parentElement
        ItemFormulario.className = "conteudo"
    }}
}



function erroInput(input,menssagem){
    const ItemFormulario = input.parentElement
    const MensageTexto = ItemFormulario.querySelector("a")
    MensageTexto.innerText = menssagem
    ItemFormulario.className = "conteudo erro"
}


function validarFormulario (){
    const ItemFormulario = formulario.querySelectorAll(".conteudo")
    const valido = [...ItemFormulario].every((item)=>{
        return item.className === "conteudo"

    })

    if (valido){
        alert("Carro cadastrado com sucesso")
        const carro = adicionarCarro()
        
        formulario.reset()

        fetch("/receber_carro",{
            method:"POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify(carro)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Resposta do servidor:', data)
            if (data.success) {
                alert('Carro cadastrado!')
                carregarCarros()
            } else {
                alert('Erro ao cadastrar.')
            }
        })
        .catch(error => console.error('Erro:', error))
    }
}




function adicionarCarro() {
    id_carro++
    return [
        parseInt(portas.value),  
        parseFloat(aluguel.value),  
        placa.value,  
        cor.value,  
        parseFloat(preco_compra.value),  
        parseInt(capacidade_pessoas.value),  
        parseInt(quilometragem.value),  
        cambio.value,  
        airbag.value === "sim_airbag",  
        ar_condicionado.value === "sim_ar_condicionado",   
        disponivel.value === "True",  
        fornecedor.value,  
        garagem.value,  
        plano_seguro.value,  
        marca.value,  
        modelo.value,  
        categoria.value,  
        combustivel.value 
    ]
}


function criarTabela (carroscadastrados){
    let tabela = "<h2>Carros cadastrados</h2><table border='1'>"
    tabela+="<tr><th>Id do carro</th><th>Marca</th><th>Modelo</th><th>Aluguel</th><th>Cor</th><th>Cambio</th><th>Portas</th><th>Airbag</th><th>Ar condicionado</th><th>Quilometragem</th><th>Combustível</th><th>Categoria</th><th>Preço de compra</th><th>Capacidade</th><th>Fornecedor</th><th>Garagem</th><th>Plano de seguro</th></tr>"
    for (const veiculo of carroscadastrados){
        tabela+=`<tr><td>${veiculo.id}</td><td>${veiculo.id_marca}</td><td>${veiculo.id_modelo}</td><td>${veiculo.aluguel}</td><td>${veiculo.cor}</td><td>${veiculo.cambio}</td><td>${veiculo.portas}</td><td>${veiculo.airbag}</td><td>${veiculo.ar_condicionado}</td><td>${veiculo.quilometragem}</td><td>${veiculo.id_combustivel}</td><td>${veiculo.id_categoria}</td><td>${veiculo.capacidade_pessoas}</td><td>${veiculo.id_fornecedor}</td><td>${veiculo.id_garagem}</td><td>${veiculo.id_plano_seguro}</td></tr>`
    }
    tabela+="</table>"
    conteudo.innerHTML = tabela
}


function carregarCarros() {
    fetch("/pegar_lista")
        .then(response => response.json())
        .then(carros => {
            criarTabela(carros);  // Passa os carros do servidor
        })} """




















""" 


def cadastrar_carro(portas, preco_diaria, placa, cor, preco_compra, capacidade_pessoas,quilometragem, cambio,airbags,ar_condicionado,disponivel,fornecedor,garagem,plano_seguro,marca,modelo,categoria,combustivel):
   try:
    fornecedor = sessao.query(Fornecedor).filter_by(nome = fornecedor).first()
    if fornecedor:
        id_fornecedor = fornecedor.id
    garagem = sessao.query(Garagem).filter_by(bairro = garagem).first()
    if garagem:
        id_garagem = garagem.id
    plano_seguro = sessao.query(PlanoSeguro).filter_by(tipo = plano_seguro).first()
    if plano_seguro:
        id_plano_seguro = plano_seguro.id
    marca = sessao.query(Marca).filter_by(nome = marca).first()
    if marca:
        id_marca = marca.id
    modelo = sessao.query(Modelo).filter_by(nome = modelo).first()
    if modelo:
        id_modelo = modelo.id
    categoria = sessao.query(Categoria).filter_by(nome = categoria).first()
    if categoria:
        id_categoria = categoria.id
    combustivel = sessao.query(Combustivel).filter_by(tipo = combustivel).first()
    if combustivel:
        id_combustivel = combustivel.id
    if id_fornecedor and id_garagem and id_plano_seguro and id_marca and id_modelo and id_categoria and id_combustivel:
        novo_carro= Veiculo(
            portas=portas,preco_diaria=preco_diaria,placa=placa, cor=cor,preco_compra=preco_compra,
              capacidade_pessoas=capacidade_pessoas, quilometragem=quilometragem, cambio=cambio, airbags=airbags,
                ar_condicionado=ar_condicionado,disponivel=disponivel, id_fornecedor=id_fornecedor,
                id_garagem=id_garagem, id_plano_seguro=id_plano_seguro, id_marca=id_marca, id_modelo=id_modelo,
                id_categoria=id_categoria, id_combustivel=id_combustivel)
        sessao.add(novo_carro)
        sessao.commit()

   except Exception as e:
    return "Erro inesperado", e
    """





""" 

@app.route("/receber_carro", methods = ["POST"])
def receber_carro():
    print("OIIIIIIIIIII")
    try:
        lista_de_atributos = request.get_json()
        cadastrar_carro(*lista_de_atributos) 
        return jsonify({"success": True, "message": "Carro cadastrado com sucesso!"})
    except Exception as erro:
        return jsonify({"success": False, "message": str(erro)}), 500 """





""" 
@app.route("/pegar_lista")
def get_carros():
    return jsonify(sessao.query(Veiculo).all())
 """