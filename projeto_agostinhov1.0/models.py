class Modelo:
    carros_cadastrados = []
    usuarios_cadastrados=[{"nome":"Admin123", "senha":"123", "admin":True}]



    

    def cadastrar_usuario(self, nome, senha, email, telefone,data_nasc,cpf,cnh):
        novo_usuario = {"nome":nome, "senha":senha,"email":email,"telefone":telefone, "data_nasc":data_nasc, "cpf":cpf,"cnh":cnh, "admin":False}
        self.usuarios_cadastrados.append(novo_usuario)


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