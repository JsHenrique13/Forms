from flask import render_template, Flask, request, redirect, flash
import json



app = Flask(__name__)
app.config['SECRET_KEY'] = "kingkey"



@app.route('/index', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def home():
    list = []
    nome = request.form.get('nome')
    print(nome)
    if request.form.get('btn') == "Add":
        list.append(nome)
    print(list)   
    return render_template("html/index.html", list=list, len = len(list))
    
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    dados = dict()
    if request.form.get('btn') == "Entrar":
        try:
            email = request.form.get('email')
            senha = request.form.get('senha')
            with open('user.json') as usuarios:
                user = json.load(usuarios)
            for c in user:
                if email == c["email"] and senha == c["senha"]:
                    return render_template("html/acesso.html")
                
        except:
            flash("Credenciais Inválidas! Tente criar uma conta")
            redirect('/login')

    if request.form.get('btn') == "Cadastrar":
        usuario = request.form.get('nvuser')
        email = request.form.get('email')
        senha0 = request.form.get('nvsenha')
        senha1 = request.form.get('cnvsenha')
        
        
        with open("user.json", "w", encoding="utf-8") as file:
            json.dump(dados, file, indent=4, sort_keys=True)
        if '@' not in email or '.com' not in email:
            flash("Email Inválido!")
            return redirect('/login')
        elif senha0 != senha1:
            flash("Senhas incoerentes!")
            return redirect('/login')
        else:
            
            usuario = request.form.get('nvuser')
            return render_template("html/valida.html", usuario=usuario)
    return render_template("html/login.html")




@app.route('/valida', methods=['GET', 'POST'])
def valida():

    return render_template("html/valida.html")



if __name__ in '__main__':
    app.run(debug=True)
