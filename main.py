from flask import render_template, Flask, request, redirect, flash
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "kingkey"


@app.route('/')
def home():
    return render_template("html/login.html")


@app.route('/cadastro', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    if request.form.get('btn') == "Entrar":
        usuario = request.form.get('user')
        return render_template("html/acesso.html", usuario=usuario)   
    if request.form.get('btn') == "Cadastrar":
        usuario = request.form.get('nvuser')
        email = request.form.get('email')
        senha0 = request.form.get('nvsenha')
        senha1 = request.form.get('cnvsenha')
        if '@' not in email or '.com' not in email:
            flash("Email Inválido!")
            return redirect('/')
        elif senha0 != senha1:
            flash("Senhas incoerentes!")
            return redirect('/')

    return render_template("html/valida.html")



@app.route('/valida')
def acesso():
    return render_template("html/valida.html")


if __name__ in '__main__':
    app.run(debug=True)
