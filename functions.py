from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    
