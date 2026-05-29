from flask import Flask, render_template, jsonify

app = Flask(__name__)

stock_carros = [
    {
        'vei_id': 1,
        'marca': 'BMW',
        'modelo': 'M4 Competition',
        'vei_preco_venda': 89900,
        'vei_ano': 2022,
        'vei_quilometros': '12.500',
        'combustivel': 'Gasolina',
        'vei_imagem': 'https://images.unsplash.com/photo-1617531653332-bd46c24f2068?w=800'
    },
    {
        'vei_id': 2,
        'marca': 'Mercedes-Benz',
        'modelo': 'AMG GT 63',
        'vei_preco_venda': 145000,
        'vei_ano': 2022,
        'vei_quilometros': '18.000',
        'combustivel': 'Gasolina',
        'vei_imagem': 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=800'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/veiculos')
def veiculos():
    return render_template('veiculos.html')

@app.route('/api/veiculos/')
def api_veiculos():
    return jsonify(stock_carros)

@app.route('/veiculo/<int:id>')
def detalhe(id):
    carro = next((c for c in stock_carros if c['vei_id'] == id), None)
    return render_template('detalhe_veiculo.html', carro=carro)

@app.route('/sobre')
def sobre():
    return render_template('SobreNos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)