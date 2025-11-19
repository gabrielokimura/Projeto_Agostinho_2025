const formulario = document.getElementById("formulario")
const marca = document.getElementById("marca")
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





function adicionarCarro(){
    id_carro++
    return [
        marca.value,
        modelo.value,
        aluguel.value,
        cor.value,
        cambio.value,
        portas.value,
        airbag.value,
        ar_condicionado.value,
        quilometragem.value, 
        combustivel.value,
        categoria.value,
        disponivel.value
    ]}


function criarTabela (carroscadastrados){
    let tabela = "<h2>Carros cadastrados</h2><table border='1'>"
    tabela+="<tr><th>Id do carro</th><th>Marca</th><th>Modelo</th><th>Aluguel</th><th>Cor</th><th>Cambio</th><th>Portas</th><th>Airbag</th><th>Ar condicionado</th><th>Quilometragem</th><th>Combustível</th><th>Categoria</th></tr>"
    for (const veiculo of carroscadastrados){
        tabela+=`<tr><td>${veiculo.id}</td><td>${veiculo.marca}</td><td>${veiculo.modelo}</td><td>${veiculo.aluguel}</td><td>${veiculo.cor}</td><td>${veiculo.cambio}</td><td>${veiculo.portas}</td><td>${veiculo.airbag}</td><td>${veiculo.ar_condicionado}</td><td>${veiculo.quilometragem}</td><td>${veiculo.combustivel}</td><td>${veiculo.categoria}</td></tr>`
    }
    tabela+="</table>"
    conteudo.innerHTML = tabela
}


function carregarCarros() {
    fetch("/pegar_lista")
        .then(response => response.json())
        .then(carros => {
            criarTabela(carros);  // Passa os carros do servidor
        })}