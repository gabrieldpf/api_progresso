from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "API de Monitoramento de Alunos",
        "description": "Documentação dos endpoints para armazenar e visualizar progresso dos alunos",
        "version": "1.0.0"
    }
})

# Armazena os dados temporariamente
dados_tempo_por_aluno_e_curso = []
dados_tempo_por_aluno = []
dados_progresso_alunos = []

@app.route('/', methods=['GET'])
def home():
    """
    Página inicial da API
    ---
    responses:
      200:
        description: Retorna uma mensagem de boas-vindas
        examples:
          application/json: "Bem-vindo à minha API Flask!"
    """
    return "Bem-vindo à minha API Flask!"

@app.route('/api/tempo_por_aluno_e_curso', methods=['POST', 'GET', 'DELETE'])
def tempo_por_aluno_e_curso():
    """
    Gerencia os dados de tempo por aluno e curso
    ---
    get:
      summary: Retorna os dados de tempo por aluno e curso
      responses:
        200:
          description: Lista dos dados armazenados
          schema:
            type: array
            items:
              type: object
              properties:
                aluno:
                  type: string
                  example: "João"
                curso:
                  type: string
                  example: "Matemática"
                tempo:
                  type: integer
                  example: 120
    post:
      summary: Adiciona novos dados de tempo por aluno e curso
      consumes:
        - application/json
      parameters:
        - in: body
          name: body
          required: true
          description: Lista de objetos contendo informações de tempo por aluno e curso
          schema:
            type: array
            items:
              type: object
              properties:
                aluno:
                  type: string
                  example: "João"
                curso:
                  type: string
                  example: "Matemática"
                tempo:
                  type: integer
                  example: 120
      responses:
        201:
          description: Dados recebidos com sucesso
          schema:
            type: object
            properties:
              mensagem:
                type: string
                example: "Dados recebidos com sucesso!"
              dados:
                type: array
                items:
                  type: object
                  example: {"aluno": "João", "curso": "Matemática", "tempo": 120}
        400:
          description: Erro por formato inválido
          schema:
            type: object
            properties:
              erro:
                type: string
                example: "Formato inválido, use JSON"
    delete:
      summary: Deleta todos os dados de tempo por aluno e curso
      responses:
        200:
          description: Dados deletados com sucesso
          schema:
            type: object
            properties:
              mensagem:
                type: string
                example: "Dados deletados com sucesso"
    """
    global dados_tempo_por_aluno_e_curso
    if request.method == 'DELETE':
        dados_tempo_por_aluno_e_curso = []
        return jsonify({'mensagem': 'Dados deletados com sucesso'}), 200
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            dados_tempo_por_aluno_e_curso.extend(data)
            return jsonify({'mensagem': 'Dados recebidos com sucesso!', 'dados': data}), 201
        else:
            return jsonify({'erro': 'Formato inválido, use JSON'}), 400
    elif request.method == 'GET':
        return jsonify(dados_tempo_por_aluno_e_curso)

@app.route('/api/tempo_por_aluno', methods=['POST', 'GET', 'DELETE'])
def tempo_por_aluno():
    """
    Gerencia os dados de tempo por aluno
    ---
    get:
      summary: Retorna os dados de tempo por aluno
      responses:
        200:
          description: Lista dos dados armazenados
          schema:
            type: array
            items:
              type: object
              properties:
                aluno:
                  type: string
                  example: "João"
                tempo:
                  type: integer
                  example: 150
    post:
      summary: Adiciona novos dados de tempo por aluno
      consumes:
        - application/json
      parameters:
        - in: body
          name: body
          required: true
          description: Lista de objetos contendo informações de tempo por aluno
          schema:
            type: array
            items:
              type: object
              properties:
                aluno:
                  type: string
                  example: "João"
                tempo:
                  type: integer
                  example: 150
      responses:
        201:
          description: Dados recebidos com sucesso
          schema:
            type: object
            properties:
              mensagem:
                type: string
                example: "Dados recebidos com sucesso!"
              dados:
                type: array
                items:
                  type: object
                  example: {"aluno": "João", "tempo": 150}
        400:
          description: Erro por formato inválido
          schema:
            type: object
            properties:
              erro:
                type: string
                example: "Formato inválido, use JSON"
    delete:
      summary: Deleta todos os dados de tempo por aluno
      responses:
        200:
          description: Dados deletados com sucesso
          schema:
            type: object
            properties:
              mensagem:
                type: string
                example: "Dados deletados com sucesso"
    """
    global dados_tempo_por_aluno
    if request.method == 'DELETE':
        dados_tempo_por_aluno = []
        return jsonify({'mensagem': 'Dados deletados com sucesso'}), 200
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            dados_tempo_por_aluno.extend(data)
            return jsonify({'mensagem': 'Dados recebidos com sucesso!', 'dados': data}), 201
        else:
            return jsonify({'erro': 'Formato inválido, use JSON'}), 400
    elif request.method == 'GET':
        return jsonify(dados_tempo_por_aluno)

@app.route('/api/progresso_por_curso', methods=['POST', 'GET', 'DELETE'])
def progresso_alunos():
    """
    Gerencia os dados de progresso dos alunos por curso
    ---
    get:
      summary: Retorna os dados de progresso dos alunos por curso
      responses:
        200:
          description: Lista dos dados armazenados
          schema:
            type: array
            items:
              type: object
              properties:
                aluno:
                  type: string
                  example: "João"
                curso:
                  type: string
                  example: "Matemática"
                progresso:
                  type: integer
                  example: 85
    post:
      summary: Adiciona novos dados de progresso por curso
      consumes:
        - application/json
      parameters:
        - in: body
          name: body
          required: true
          description: Lista de objetos contendo informações de progresso por curso
          schema:
            type: array
            items:
              type: object
              properties:
                aluno:
                  type: string
                  example: "João"
                curso:
                  type: string
                  example: "Matemática"
                progresso:
                  type: integer
                  example: 85
      responses:
        201:
          description: Dados recebidos com sucesso
          schema:
            type: object
            properties:
              mensagem:
                type: string
                example: "Dados recebidos com sucesso!"
              dados:
                type: array
                items:
                  type: object
                  example: {"aluno": "João", "curso": "Matemática", "progresso": 85}
        400:
          description: Erro por formato inválido
          schema:
            type: object
            properties:
              erro:
                type: string
                example: "Formato inválido, use JSON"
    delete:
      summary: Deleta todos os dados de progresso dos alunos
      responses:
        200:
          description: Dados deletados com sucesso
          schema:
            type: object
            properties:
              mensagem:
                type: string
                example: "Dados deletados com sucesso"
    """
    global dados_progresso_alunos
    if request.method == 'DELETE':
        dados_progresso_alunos = []
        return jsonify({'mensagem': 'Dados deletados com sucesso'}), 200
    elif request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            dados_progresso_alunos.extend(data)
            return jsonify({'mensagem': 'Dados recebidos com sucesso!', 'dados': data}), 201
        else:
            return jsonify({'erro': 'Formato inválido, use JSON'}), 400
    elif request.method == 'GET':
        return jsonify(dados_progresso_alunos)

if __name__ == '__main__':
    app.run(debug=True)