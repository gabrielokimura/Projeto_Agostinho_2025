from flask import Flask, render_template, redirect, url_for, request, make_response, session

app = Flask(__name__)

app.secret_key="123"            

usuarios_cadastrados=[]

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    mensagem= None
    if request.method=="POST":
        if "nome"  in request.form and "senha" in request.form:
            session["nome"]=request.form["nome"]
            mensagem = session["nome"]
            session["senha"] = request.form["senha"]
        else:
            mensagem = "Bota o nome E a senha idiota"


    return render_template("cadastro.html", mensagem = mensagem)



if __name__=="__main__":
    app.run(debug=True)