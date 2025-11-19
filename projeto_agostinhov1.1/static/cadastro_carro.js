const formulario = document.getElementById("formulario")
const marca = document.getElementById("marca")
const placa = document.getElementById("placa")
const modelo = document.getElementById("modelo")
const aluguel = document.getElementById("aluguel")  // ID corrigido
const cor = document.getElementById("cor")
const cambio = document.getElementById("cambio")
const portas = document.getElementById("portas")
const airbag = document.getElementById("airbag")
const ar_condicionado = document.getElementById("ar_condicionado")
const combustivel = document.getElementById("combustivel")
const quilometragem = document.getElementById("quilometragem")
const categoria = document.getElementById("categoria")
const preco_compra = document.getElementById("preco_compra")
const capacidade_pessoas = document.getElementById("capacidade_pessoas")
const fornecedor = document.getElementById("fornecedor")
const garagem = document.getElementById("garagem")
const plano_seguro = document.getElementById("plano_seguro")
const disponivel = document.getElementById("disponivel")
const CAMPOS = [marca, placa, modelo, aluguel, cor, cambio, portas, airbag, ar_condicionado, combustivel, quilometragem, categoria, preco_compra, capacidade_pessoas, fornecedor, garagem, plano_seguro, disponivel]
const conteudo = document.getElementById("carros_cadastrados")

document.addEventListener("DOMContentLoaded", carregarCarros)

formulario.addEventListener("submit", (event) => {
    event.preventDefault()
    checarcampos()
    validarFormulario()
})

function checarcampos() {
    for (let campo of CAMPOS) {
        const valor = campo.value
        if (valor == "") {
            erroInput(campo, "O campo " + campo.id + " é obrigatório")
        } else {
            const ItemFormulario = campo.parentElement
            ItemFormulario.className = "conteudo"
        }
    }
}

function erroInput(input, menssagem) {
    const ItemFormulario = input.parentElement
    const MensageTexto = ItemFormulario.querySelector("a")
    if (MensageTexto) {
        MensageTexto.innerText = menssagem
    }
    ItemFormulario.className = "conteudo erro"
}

function validarFormulario() {
    const ItemFormulario = formulario.querySelectorAll(".conteudo")
    const valido = [...ItemFormulario].every((item) => {
        return item.className === "conteudo"
    })

    if (valido) {
        alert("Carro cadastrado com sucesso")
        const carro = adicionarCarro()
        formulario.reset()

        fetch("/receber_carro", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(carro)
        })
        .then(response => {
            console.log('Status da resposta:', response.status)
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`)
            }
            return response.json()
        })
        .then(data => {
            console.log('Resposta do servidor:', data)
            if (data.success) {
                alert('Carro cadastrado!')
                carregarCarros()  // Atualiza tabela dinamicamente
            } else {
                alert('Erro ao cadastrar: ' + data.message)
            }
        })
        .catch(error => {
            console.error('Erro no fetch:', error)
            alert('Erro ao enviar dados: ' + error.message)
        })
    }
}

function adicionarCarro() {
    return {
        portas: parseInt(portas.value),
        preco_diaria: parseFloat(aluguel.value),
        placa: placa.value,
        cor: cor.value,
        preco_compra: parseFloat(preco_compra.value),
        capacidade_pessoas: parseInt(capacidade_pessoas.value),
        quilometragem: parseInt(quilometragem.value),
        cambio: cambio.value,
        airbags: airbag.value === "sim_airbag",
        ar_condicionado: ar_condicionado.value === "sim_ar_condicionado",
        disponivel: disponivel.value === "True",
        fornecedor: fornecedor.value,
        garagem: garagem.value,
        plano_seguro: plano_seguro.value,
        marca: marca.value,
        modelo: modelo.value,
        categoria: categoria.value,
        combustivel: combustivel.value
    }
}

function criarTabela(carros) {
    let tabela = "<h2>Carros Cadastrados</h2><table border='1'>"
    tabela += "<tr><th>ID</th><th>Placa</th><th>Marca</th><th>Modelo</th><th>Preço Diária</th><th>Cor</th><th>Câmbio</th><th>Portas</th><th>Airbags</th><th>Ar Condicionado</th><th>Quilometragem</th><th>Combustível</th><th>Categoria</th><th>Preço Compra</th><th>Capacidade</th><th>Fornecedor</th><th>Garagem</th><th>Plano Seguro</th></tr>"
    for (const carro of carros) {
        tabela += `<tr><td>${carro.id}</td><td>${carro.placa}</td><td>${carro.id_marca}</td><td>${carro.id_modelo}</td><td>${carro.preco_diaria}</td><td>${carro.cor}</td><td>${carro.cambio}</td><td>${carro.portas}</td><td>${carro.airbags}</td><td>${carro.ar_condicionado}</td><td>${carro.quilometragem}</td><td>${carro.id_combustivel}</td><td>${carro.id_categoria}</td><td>${carro.preco_compra}</td><td>${carro.capacidade_pessoas}</td><td>${carro.id_fornecedor}</td><td>${carro.id_garagem}</td><td>${carro.id_plano_seguro}</td></tr>`
    }
    tabela += "</table>"
    conteudo.innerHTML = tabela
}

function carregarCarros() {
    fetch("/pegar_lista")
        .then(response => response.json())
        .then(carros => {
            criarTabela(carros)
        })
        .catch(error => console.error('Erro ao carregar carros:', error))
}