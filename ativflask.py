from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'explicação decorator' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Um decorator é um padrão de projeto estrutural, comum em linguagens como Python e TypeScript, que permite adicionar funcionalidades a funções, métodos ou classes existentes de forma dinâmica, sem alterar seu código original. Eles "embrulham" (wrap) o comportamento original, executando códigos antes ou depois da função principal.' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento