from flask import Flask, request, jsonify
import os
from datetime import datetime
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app, resources={r"/registrar": {"origins": "*", "methods": ["POST"]}})

ARQUIVO_TXT = Path("/storage/emulated/0/Documents/registros.txt")

ARQUIVO_TXT.parent.mkdir(parents=True, exist_ok=True)

if not ARQUIVO_TXT.exists():
    print("Arquivo TXT não encontrado, criando um novo...")
    with open(ARQUIVO_TXT, 'w', encoding='utf-8') as f:
        f.write("Nome|Cidade|Idade|Data|Tema\n")

@app.route('/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    print("Dados recebidos:", dados)
    print("Salvando em:", ARQUIVO_TXT)  
    
    nome = dados.get("visitante", "").strip()
    cidade = dados.get("cidade", "").strip()
    idade = dados.get("idade", "").strip()
    tema = dados.get("tema", "Exposição: 60 anos do Instituto").strip()
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    if not nome or not cidade:
        return jsonify({"status": "erro", "mensagem": "Campos obrigatórios faltando"}), 400

    try:
        with open(ARQUIVO_TXT, 'a', encoding='utf-8') as f:
            f.write(f"{nome}|{cidade}|{idade}|{data}|{tema}\n")
        print("Registro salvo com sucesso em:", ARQUIVO_TXT)
        
    except Exception as e:
        print("Erro ao salvar no TXT:", e)
        return jsonify({"status": "erro", "mensagem": "Erro ao salvar registro"}), 500

    return jsonify({"status": "sucesso", "mensagem": "Registro salvo com sucesso!"}), 200

@app.route('/')
def status():
    return jsonify({
        "status": "servidor_rodando",
        "arquivo_salvo_em": str(ARQUIVO_TXT),
        "arquivo_existe": ARQUIVO_TXT.exists(),
        "ultima_modificacao": datetime.fromtimestamp(ARQUIVO_TXT.stat().st_mtime).strftime("%d/%m/%Y %H:%M") if ARQUIVO_TXT.exists() else "n/a"
    })

if __name__ == '__main__':
    print("Iniciando o servidor Flask...")
    print("📁 Arquivo será salvo em:", ARQUIVO_TXT)
    print("📂 Pasta existe?", ARQUIVO_TXT.parent.exists())
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))