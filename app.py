# api -> lugar para disponibilizar recursos ou funcionalidades

#objetivo -> api que disponibiliza consulta, cruiação, edicao e exclusao de livros

#URL BASE --> LOCALHOST
#ENDPOINTS -> localhost/livros(GET), localhost/livros/ID(GET), localhost/livros/ID(PUT), localhost/livros/ID(DELETE)

#QUAIS RECURSOS -> Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Clube da luta',
        'autor': 'zé',
    },
    {
        'id': 2,
        'titulo': 'Clube da luta',
        'autor': 'zé',
    },
    {
        'id': 3,
        'titulo': 'Clube da luta',
        'autor': 'zé',
    },
]

#Consuultar todos
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#CONSULTAR ID:
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar 
@app.route('/livros',methods=['POST'])
def inserir_livro():
    livro_novo = request.get_json()

    livros.append(livro_novo)

    return jsonify(livros)

#deletar
@app.route('/livros/<int:id>',methods=['DELETE'])

def deletar_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)            



app.run(port=5000, host='localhost', debug=True)