# API do Progresso dos Alunos

Bem-vindo ao repositório da API de Monitoramento de Alunos. Esta API foi desenvolvida com Flask e Flasgger para gerenciar e visualizar o progresso de alunos em cursos, incluindo o tempo gasto por aluno e curso, tempo total por aluno e progresso por curso.

## Funcionalidades da API

A API possui três endpoints principais, todos suportando os métodos HTTP `GET`, `POST` e `DELETE`:

1. **`/api/tempo_por_aluno_e_curso`**
   - **GET**: Retorna a lista de dados de tempo gasto por aluno em cada curso.
   - **POST**: Adiciona novos registros de tempo por aluno e curso (formato JSON).
   - **DELETE**: Remove todos os dados armazenados neste endpoint.
   - Exemplo de entrada: `[{"aluno": "João", "curso": "Matemática", "tempo": 120}]`

2. **`/api/tempo_por_aluno`**
   - **GET**: Retorna a lista de tempo total gasto por aluno.
   - **POST**: Adiciona novos registros de tempo por aluno (formato JSON).
   - **DELETE**: Remove todos os dados armazenados neste endpoint.
   - Exemplo de entrada: `[{"aluno": "João", "tempo": 150}]`

3. **`/api/progresso_por_curso`**
   - **GET**: Retorna a lista de progresso dos alunos por curso.
   - **POST**: Adiciona novos registros de progresso por curso (formato JSON).
   - **DELETE**: Remove todos os dados armazenados neste endpoint.
   - Exemplo de entrada: `[{"aluno": "João", "curso": "Matemática", "progresso": 85}]`

A documentação dos endpoints está disponível via Swagger em `/apidocs` quando a API estiver rodando.

## Contato
- **Responsável**: Gabriel Fonseca
- **Email**: [gabrielfonseca@projetodesenvolve.com.br]

## Porta
A API roda na porta padrão do Flask, que é **5000**. Caso precise alterar, modifique o parâmetro `port` no método `app.run()` no arquivo `app.py`.

## Pré-requisitos
- Python 3.x instalado
- Bibliotecas necessárias:
  - Flask
  - Flasgger

Instale as dependências com:
```bash
pip install flask flasgger
