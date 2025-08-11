from flask import Flask, request, jsonify
from openpyxl import Workbook, load_workbook
import os
from datetime import datetime

app = Flask(__name__)

ARQUIVO_EXCEL = "registros.xlsx"

# Criar o arquivo com cabeçalho, se não existir
if not os.path.exists(ARQUIVO_EXCEL):
    wb = Workbook()
    ws = wb.active
    ws.title = "Visitantes"
    ws.append(["Nome", "Cidade", "Idade", "Data", "Tema"])
    wb.save(ARQUIVO_EXCEL)

@app.route('/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()

    nome = dados.get("visitante", "").strip()
    cidade = dados.get("cidade", "").strip()
    idade = dados.get("idade", "").strip()
    tema = dados.get("tema", "Exposição: 60 anos do Instituto").strip()
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    if not nome or not cidade:
        return jsonify({"status": "erro", "mensagem": "Campos obrigatórios faltando"}), 400

    wb = load_workbook(ARQUIVO_EXCEL)
    ws = wb.active
    ws.append([nome, cidade, idade, data, tema])
    wb.save(ARQUIVO_EXCEL)

    return jsonify({"status": "sucesso", "mensagem": "Registro adicionado!"})

if __name__ == "__main__":
    app.run(debug=True)
