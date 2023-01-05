from flask import render_template, Flask, request, redirect, flash
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "kingkey"


@app.route('/')
def home():
    return render_template("html/index.html")


@app.route('/cadastro', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    if request.form.get('btn') == "Entrar":
        usuario = request.form.get('user')
        
    if request.form.get('btn') == "Cadastrar":
        usuario = request.form.get('nvuser')
        email = request.form.get('email')
        senha0 = request.form.get('nvsenha')
        senha1 = request.form.get('cnvsenha')
        if '@' not in email or '.com' not in email:
            flash("Email Inválido!")
            return redirect('/')
        if senha0 != senha1:
            flash("Senhas incoerentes!")
            return redirect('/')

    return render_template("html/acesso.html", usuario=usuario)



"""@app.route('/acesso')
def acesso():
    return render_template("html/acesso.html", usuario = usuario)
"""

if __name__ in '__main__':
    app.run(debug=True)
