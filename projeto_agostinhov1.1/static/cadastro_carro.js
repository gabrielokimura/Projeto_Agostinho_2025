document.addEventListener("DOMContentLoaded", () => {
    

    const formulario = document.getElementById("formulario")
    const marca = document.getElementById("marca")
    const placa = document.getElementById("placa")
    const modelo = document.getElementById("modelo")
    const preco_diaria = document.getElementById("preco_diaria")
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
    const CAMPOS = [marca, placa, modelo, preco_diaria, cor, cambio, portas, airbag, ar_condicionado, combustivel, quilometragem, categoria, preco_compra, capacidade_pessoas, fornecedor, garagem, plano_seguro, disponivel]
    const conteudo = document.getElementById("carros_cadastrados")

  
    const modelosPorMarca = {
        "1": [1, 2, 3, 4, 5],  
        "2": [6, 7, 8, 9, 10],  
        "3": [11, 12, 13, 14, 15],  
        "4": [16, 17, 18, 19, 20],  
        "5": [21, 22, 23, 24, 25]  
    }


    const nomesModelos = {
        1: "Argo", 2: "Cronos", 3: "Pulse", 4: "Strada", 5: "Mobi",
        6: "Onix", 7: "Tracker", 8: "S10", 9: "Spin", 10: "Bolt EV",
        11: "Polo", 12: "Nivus", 13: "T-Cross", 14: "Jetta", 15: "Amarok",
        16: "Corolla", 17: "Corolla Cross", 18: "Hilux", 19: "Yaris Hatch", 20: "SW4",
        21: "HB20", 22: "Creta", 23: "HB20S", 24: "Tucson", 25: "IONIQ 5"
    }


    marca.addEventListener("change", () => {
        const marcaSelecionada = marca.value
        modelo.innerHTML = '<option value="">Selecione um modelo</option>' 
        if (modelosPorMarca[marcaSelecionada]) {
            modelosPorMarca[marcaSelecionada].forEach(modeloId => {
                const option = document.createElement("option")
                option.value = modeloId
                option.textContent = nomesModelos[modeloId]
                modelo.appendChild(option)
            })
        }
    })

    for (let campo of CAMPOS) {
        if (!campo) {
            console.error(`Campo não encontrado: verifique o ID no HTML para ${campo ? campo.id : 'campo indefinido'}`)
            throw new Error("Campo obrigatório não encontrado no DOM")
        }
    }

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
                    alert('Carro cadastrado com sucesso!')
                    carregarCarros()
                } else {
                    alert('Erro ao cadastrar: ' + data.message)
                }
            })
            .catch(error => {
                console.error('Erro no fetch:', error)
                alert('Erro ao enviar dados: ' + error.message)
            })
        } else {
            console.log("Validação falhou - campos vazios ou inválidos")
        }
    }

    function adicionarCarro() {
        return [
            parseInt(portas.value),
            parseFloat(preco_diaria.value),
            placa.value,
            cor.value,
            parseFloat(preco_compra.value),
            parseInt(capacidade_pessoas.value),
            parseInt(quilometragem.value),
            cambio.value,
            airbag.value === "sim",
            ar_condicionado.value === "sim",
            disponivel.value === "sim",
            fornecedor.value,
            garagem.value,
            plano_seguro.value,
            marca.value,  
            modelo.value, 
            categoria.value,
            combustivel.value
        ]
    }

    function criarTabela(carros) {
        let tabela = "<h2>Carros Cadastrados</h2><table border='1'>"
        tabela += "<tr><th>ID</th><th>Placa</th><th>Marca</th><th>Modelo</th><th>Preço Diária</th><th>Cor</th><th>Câmbio</th><th>Portas</th><th>Airbags</th><th>Ar Condicionado</th><th>Quilometragem</th><th>Combustível</th><th>Categoria</th><th>Preço Compra</th><th>Capacidade</th><th>Fornecedor</th><th>Garagem</th><th>Plano Seguro</th></tr>"
        for (const carro of carros) {
            tabela += `<tr><td>${carro.id}</td><td>${carro.placa}</td><td>${carro.marca}</td><td>${carro.modelo}</td><td>${carro.preco_diaria}</td><td>${carro.cor}</td><td>${carro.cambio}</td><td>${carro.portas}</td><td>${carro.airbags}</td><td>${carro.ar_condicionado}</td><td>${carro.quilometragem}</td><td>${carro.combustivel}</td><td>${carro.categoria}</td><td>${carro.preco_compra}</td><td>${carro.capacidade_pessoas}</td><td>${carro.fornecedor}</td><td>${carro.garagem}</td><td>${carro.plano_seguro}</td></tr>`
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

    carregarCarros()
})