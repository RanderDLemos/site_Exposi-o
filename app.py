from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

# Configuração CORRETA do CORS
CORS(app, resources={r"/registrar": {"origins": "*"}})

# Configurações do MySQL CORRETAS
MYSQL_CONFIG = {
    'host': 'localhost',
    'database': 'exposicao_inatel',
    'user': 'usuario_inatel',
    'password': 'UsuarioInatel',
    'auth_plugin': 'mysql_native_password'
}

def criar_conexao():
    try:
        conexao = mysql.connector.connect(**MYSQL_CONFIG)
        if conexao.is_connected():
            return conexao
    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
    return None

def criar_tabela():
    conexao = criar_conexao()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS visitantes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    cidade VARCHAR(255) NOT NULL,
                    idade INT,
                    data_registro DATETIME NOT NULL,
                    tema VARCHAR(255) DEFAULT 'Exposição: 60 anos do Instituto'
                )
            """)
            print("Tabela 'visitantes' verificada/criada com sucesso")
            conexao.commit()
        except Error as e:
            print("Erro ao criar tabela:", e)
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

# Criar a tabela quando a aplicação iniciar
criar_tabela()

@app.route('/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    print("Dados recebidos:", dados)
    
    nome = dados.get("visitante", "").strip()
    cidade = dados.get("cidade", "").strip()
    idade = dados.get("idade", "").strip()
    tema = dados.get("tema", "Exposição: 60 anos do Instituto").strip()
    data = datetime.now()

    if not nome or not cidade:
        return jsonify({"status": "erro", "mensagem": "Campos obrigatórios faltando"}), 400

    try:
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor()
            
            # Converter idade para inteiro ou None se estiver vazia
            idade_int = int(idade) if idade.isdigit() else None
            
            query = "INSERT INTO visitantes (nome, cidade, idade, data_registro, tema) VALUES (%s, %s, %s, %s, %s)"
            valores = (nome, cidade, idade_int, data, tema)
            
            cursor.execute(query, valores)
            conexao.commit()
            
            print("Registro salvo no MySQL com sucesso!")
            return jsonify({"status": "sucesso", "mensagem": "Registro salvo com sucesso!"}), 200
        else:
            return jsonify({"status": "erro", "mensagem": "Erro de conexão com o banco de dados"}), 500
            
    except Error as e:
        print("Erro ao salvar no MySQL:", e)
        return jsonify({"status": "erro", "mensagem": "Erro ao salvar registro"}), 500
    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

@app.route('/visitantes', methods=['GET'])
def listar_visitantes():
    try:
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT nome, cidade, idade, data_registro, tema FROM visitantes ORDER BY data_registro DESC")
            resultados = cursor.fetchall()
            
            # Converter datetime para string
            for resultado in resultados:
                if resultado['data_registro']:
                    resultado['data_registro'] = resultado['data_registro'].strftime("%d/%m/%Y %H:%M")
            
            return jsonify({"status": "sucesso", "visitantes": resultados}), 200
        else:
            return jsonify({"status": "erro", "mensagem": "Erro de conexão com o banco de dados"}), 500
            
    except Error as e:
        print("Erro ao buscar visitantes:", e)
        return jsonify({"status": "erro", "mensagem": "Erro ao buscar registros"}), 500
    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

if __name__ == '__main__':
    print("Iniciando o servidor Flask com MySQL...")
    app.run(host='0.0.0.0', port=5001, debug=True)