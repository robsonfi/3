from flask import Flask, request, jsonify

app = Flask(__name__)

descontos = {
    1: 0.05,
    2: 0.15,
    3: 0.07,
    4: 0.12,
    5: 0.20
}

@app.route('/calcular_desconto', methods=['POST'])
def calcular_desconto():
    dados = request.json
    preco = dados.get('preco')
    codigo_origem = dados.get('codigo_origem')
    
    desconto = descontos.get(codigo_origem, 0)
    preco_com_desconto = preco * (1 - desconto)
    
    return jsonify({"preco_final": preco_com_desconto})

if __name__ == '__main__':
    app.run(debug=True)
