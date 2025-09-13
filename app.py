from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='API de Gerenciamento de Usuários',
    description='API RESTful simples para gerenciar usuários com operações CRUD',
    doc='/docs/',  
    contact='Grupo 4 - DAM IMPACTA',
    contact_email='grupo4@impacta.edu.br'
)


ns = api.namespace('users', description='Operações com usuários')


user_model = api.model('User', {
    'id': fields.Integer(readonly=True, description='ID único do usuário'),
    'nome': fields.String(required=True, description='Nome completo do usuário', example='Anna Julia Higa Farincho'),
    'email': fields.String(required=True, description='Email do usuário', example='anna.julia@email.com')
})

user_input_model = api.model('UserInput', {
    'nome': fields.String(required=True, description='Nome completo do usuário', example='Anna Julia Higa Farincho'),
    'email': fields.String(required=True, description='Email do usuário', example='anna.julia@email.com')
})


error_model = api.model('Error', {
    'error': fields.String(description='Mensagem de erro', example='Usuário não encontrado')
})

success_model = api.model('Success', {
    'message': fields.String(description='Mensagem de sucesso', example='Usuário excluído com sucesso')
})


users = [
    {'id': 1, 'nome': 'Anna Julia Higa Farincho', 'email': 'anna.julia@email.com'},
    {'id': 2, 'nome': 'Letícia Macedo', 'email': 'leticia.macedo@email.com'},
    {'id': 3, 'nome': 'Evelyn Mercês', 'email': 'evelyn.merces@email.com'}
]
next_id = 4

def find_user(user_id):
    
    return next((user for user in users if user['id'] == user_id), None)

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    @ns.response(200, 'Lista de usuários retornada com sucesso')
    def get(self):
        return users

    @ns.doc('create_user')
    @ns.expect(user_input_model, validate=True)
    @ns.marshal_with(user_model, code=201)
    @ns.response(201, 'Usuário criado com sucesso')
    @ns.response(400, 'Dados inválidos', error_model)
    def post(self):
        
        global next_id
        
        data = request.get_json()
        
        
        if not data or 'nome' not in data or 'email' not in data:
            api.abort(400, 'Nome e email são obrigatórios')
        
        if not data['nome'].strip() or not data['email'].strip():
            api.abort(400, 'Nome e email não podem estar vazios')
        
        
        if any(user['email'].lower() == data['email'].lower() for user in users):
            api.abort(400, 'Email já está em uso')
        
        new_user = {
            'id': next_id,
            'nome': data['nome'].strip(),
            'email': data['email'].strip()
        }
        
        users.append(new_user)
        next_id += 1
        
        return new_user, 201

@ns.route('/<int:user_id>')
@ns.param('user_id', 'Identificador único do usuário')
class User(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    @ns.response(200, 'Usuário encontrado')
    @ns.response(404, 'Usuário não encontrado', error_model)
    def get(self, user_id):
        user = find_user(user_id)
        if not user:
            api.abort(404, 'Usuário não encontrado')
        return user

    @ns.doc('update_user')
    @ns.expect(user_input_model, validate=True)
    @ns.marshal_with(user_model)
    @ns.response(200, 'Usuário atualizado com sucesso')
    @ns.response(404, 'Usuário não encontrado', error_model)
    @ns.response(400, 'Dados inválidos', error_model)
    def put(self, user_id):
        user = find_user(user_id)
        if not user:
            api.abort(404, 'Usuário não encontrado')
        
        data = request.get_json()
        
        if not data or 'nome' not in data or 'email' not in data:
            api.abort(400, 'Nome e email são obrigatórios')
        
        if not data['nome'].strip() or not data['email'].strip():
            api.abort(400, 'Nome e email não podem estar vazios')
        
       
        existing_user = next((u for u in users if u['email'].lower() == data['email'].lower() and u['id'] != user_id), None)
        if existing_user:
            api.abort(400, 'Email já está em uso por outro usuário')
        
       
        user['nome'] = data['nome'].strip()
        user['email'] = data['email'].strip()
        
        return user

    @ns.doc('delete_user')
    @ns.response(200, 'Usuário excluído com sucesso', success_model)
    @ns.response(404, 'Usuário não encontrado', error_model)
    def delete(self, user_id):
        user = find_user(user_id)
        if not user:
            api.abort(404, 'Usuário não encontrado')
        
        users.remove(user)
        return {'message': 'Usuário excluído com sucesso'}

@api.route('/info')
class ApiInfo(Resource):
    @api.doc('api_info')
    def get(self):
        return {
            'name': 'API de Gerenciamento de Usuários',
            'version': '1.0',
            'description': 'API RESTful simples para gerenciar usuários',
            'authors': ['Anna Julia Higa Farincho', 'Letícia Macedo', 'Evelyn Mercês'],
            'grupo': 4,
            'instituicao': 'IMPACTA',
            'disciplina': 'Desenvolvimento de APIs e Microserviços (DAM)',
            'endpoints': {
                'GET /users': 'Listar todos os usuários',
                'POST /users': 'Criar novo usuário',
                'GET /users/<id>': 'Buscar usuário específico',
                'PUT /users/<id>': 'Atualizar usuário',
                'DELETE /users/<id>': 'Excluir usuário'
            }
        }

if __name__ == '__main__':
    print("=== API de Gerenciamento de Usuários ===")
    print("Desenvolvido por: Anna Julia Higa Farincho, Letícia Macedo, Evelyn Mercês")
    print("Grupo: 4 | Instituição: IMPACTA")
    print("Disciplina: Desenvolvimento de APIs e Microserviços (DAM)")
    print("\nDocumentação Swagger disponível em: http://localhost:5000/docs/")
    print("API rodando em: http://localhost:5000")
    
    app.run(debug=True)