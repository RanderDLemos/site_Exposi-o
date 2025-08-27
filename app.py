from flask import Flask, request, jsonify
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/registrar": {"origins": "*", "methods": ["POST"]}})

ARQUIVO_TXT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "registros.txt")

# Criar arquivo se não existir
if not os.path.exists(ARQUIVO_TXT):
    print("Arquivo TXT não encontrado, criando um novo...")
    with open(ARQUIVO_TXT, 'w', encoding='utf-8') as f:
        f.write("Nome|Cidade|Idade|Data|Tema\n")

@app.route('/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    print("Dados recebidos:", dados)
    nome = dados.get("visitante", "").strip()
    cidade = dados.get("cidade", "").strip()
    idade = dados.get("idade", "").strip()
    tema = dados.get("tema", "Exposição: 60 anos do Instituto").strip()
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    if not nome or not cidade:
        return jsonify({"status": "erro", "mensagem": "Campos obrigatórios faltando"}), 400

    try:
        # Salvar no arquivo TXT (formato CSV com pipe como separador)
        with open(ARQUIVO_TXT, 'a', encoding='utf-8') as f:
            f.write(f"{nome}|{cidade}|{idade}|{data}|{tema}\n")
        print("Registro salvo com sucesso!")
        
    except Exception as e:
        print("Erro ao salvar no TXT:", e)
        return jsonify({"status": "erro", "mensagem": "Erro ao salvar registro"}), 500

    return jsonify({"status": "sucesso", "mensagem": "Registro salvo com sucesso!"}), 200
    
if __name__ == '__main__':
    print("Iniciando o servidor Flask...")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))