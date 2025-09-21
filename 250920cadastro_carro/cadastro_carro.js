const formulario = document.getElementById("formulario")
const marca = document.getElementById("marca")
const modelo = document.getElementById("modelo")
const aluguel = document.getElementById("aluguel")
const cor = document.getElementById("cor")
const cambio = document.getElementById("cambio")
const portas = document.getElementById("portas")
const carroscadastrados = []
const conteudo = document.getElementById("carros_cadastrados")

formulario.addEventListener("submit", (event) =>{
    event.preventDefault()

    checar(marca)
    checar(modelo)
    checar(aluguel)
    checar(cor)
    checar(cambio)
    checar(portas)
    validarFormulario()


    
})


function checar(campo){
    const valor = campo.value
    if (valor == ""){
        erroInput(campo, "O campo "+campo.id+" é obrigatório")
    } else {
        const ItemFormulario = campo.parentElement
        ItemFormulario.className = "conteudo"
    }
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
        var carro = adicionarCarro()
        carroscadastrados.push(carro)
        criarTabela()
        formulario.reset()
    }
}





function adicionarCarro(){
    return{
        "marca":marca.value,
        "modelo":modelo.value,
        "aluguel":aluguel.value,
        "cor":cor.value,
        "cambio":cambio.value,
        "portas":portas.value
    }
}


function criarTabela (){
    let tabela = "<h2>Carros cadastrados</h2><table border='1'>"
    tabela+="<tr><th>Marca</th><th>Modelo</th><th>Aluguel</th><th>Cor</th><th>Cambio</th><th>Portas</th></tr>"
    for (const veiculo of carroscadastrados){
        tabela+=`<tr><td>${veiculo.marca}</td><td>${veiculo.modelo}</td><td>${veiculo.aluguel}</td><td>${veiculo.cor}</td><td>${veiculo.cambio}</td><td>${veiculo.portas}</td></tr>`
    }
    tabela+="</table>"
    conteudo.innerHTML = tabela
}