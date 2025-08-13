from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Isso permite requisições do seu frontend

@app.route('/registrar', methods=['POST'])
def registrar():
    try:
        dados = request.get_json()
        
        # Validação básica
        if not dados or 'visitante' not in dados or 'cidade' not in dados:
            return jsonify({
                'status': 'erro',
                'message': 'Dados incompletos'
            }), 400
        
        # Aqui você processaria os dados (salvar em banco de dados, etc.)
        print(f"Novo registro: {dados}")
        
        return jsonify({
            'status': 'sucesso',
            'message': 'Registro realizado com sucesso'
        })
        
    except Exception as e:
        return jsonify({
            'status': 'erro',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))