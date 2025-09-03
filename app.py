from flask import Flask, request, jsonify, send_from_directory
import os
from datetime import datetime
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Caminho do arquivo TXT (na pasta Documents visível)
ARQUIVO_TXT = Path("/storage/emulated/0/Documents/registros.txt")
ARQUIVO_TXT.parent.mkdir(parents=True, exist_ok=True)

if not ARQUIVO_TXT.exists():
    with open(ARQUIVO_TXT, 'w', encoding='utf-8') as f:
        f.write("Nome|Cidade|Idade|Data|Tema\n")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    
    nome = dados.get("visitante", "").strip()
    cidade = dados.get("cidade", "").strip()
    idade = dados.get("idade", "").strip()
    tema = dados.get("tema", "Exposição: 60 anos do Instituto").strip()
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    if not nome or not cidade:
        return jsonify({"status": "erro", "mensagem": "Nome e cidade são obrigatórios"}), 400

    try:
        with open(ARQUIVO_TXT, 'a', encoding='utf-8') as f:
            f.write(f"{nome}|{cidade}|{idade}|{data}|{tema}\n")
        return jsonify({"status": "sucesso", "mensagem": "Registro salvo!"}), 200
        
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": "Erro ao salvar"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)