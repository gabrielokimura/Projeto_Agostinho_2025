

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

