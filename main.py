from flask import render_template, Flask, request, redirect, flash
import json
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



app = Flask(__name__)
app.config['SECRET_KEY'] = "kingkey"


"""with open("user.json", "w", encoding="utf-8") as file:
    json.dump("", file, indent=4, sort_keys=True)

"""
def geracodigo():
    n = randint(000000, 999999)
    return str(n)


def saveuser(dados):
    arquivo = "user.json"
      
    try:
        with open(arquivo, "w", encoding="utf-8") as file:
            json.dump(dados, file, indent=4, sort_keys=True)
            
    except: pass
    

def pegakey():
    try:
        with open("user.json") as file:
            info = json.load(file)
            codigo = info["chave"]
            return codigo
    except:pass
    


def pegauser():
    try:
        with open("user.json") as file:
            info = json.load(file)
            user = info["nome"]
            return user 
    except:pass
       

def enviacodigo(codigo):
    try:
        with open("user.json") as file:
            info = json.load(file)
            email = info["email"]
            inicio = "jshenrique@assesi.com"
            msg = MIMEMultipart()
            msg['From'] = inicio
            msg['To'] = email
            msg['Subject'] = "Chave de Validação de Usuário"
            body = f"""
            <h2 style="margin-top: 0;">
                <span style="background-color:#d00000; border-radius: 20px; padding: 7px; ">Sua chave é : {codigo}</span>
            </h2>"""

            msg.attach(MIMEText(body, 'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)    # setando conexçao com o host do gmail
            server.starttls()   # iniciando a conexão
            server.login(inicio, "mdyxmxrjqtxdaogz")  # logando com o email que vai enviar o email
            text = msg.as_string()  # codificando as informações pro formato de leitura do gmail
            server.sendmail(inicio, email, text)  # enviando as informações
            server.quit()
            print('email enviado')
    except Exception as erro : print(f'erro ao enviar {erro}')
    


@app.route('/index')
@app.route('/')
def home():
    return render_template("html/index.html")



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
                    return render_template("html/acesso.html", usuario=pegauser())
                
        except:
            flash("Credenciais Inválidas! Tente criar uma conta")
            redirect('/login')

    if request.form.get('btn') == "Cadastrar":
        usuario = request.form.get('nvuser')
        email = request.form.get('email')
        senha0 = request.form.get('nvsenha')
        senha1 = request.form.get('cnvsenha')
        #   dados.update("nome", usuario)
        #   dados.update("email", email)
        #   dados.update("senha", senha0)
        #   dados.update("chave", geracodigo())
        dados["nome"] = usuario
        dados["email"] = email
        dados["senha"] = senha0
        dados["chave"] = geracodigo()
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
    usuario = pegauser()
    codigo = pegakey()
    enviacodigo(codigo)
    chave = request.form.get('codigo')
    if codigo == chave:
        return render_template("html/acesso.html", usuario=usuario)
    return render_template("html/valida.html")


if __name__ in '__main__':
    app.run(debug=True)
