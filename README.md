# API de Gerenciamento de Usuários com Swagger

API RESTful simples desenvolvida com Flask para gerenciar usuários com operações CRUD, agora com documentação automática usando Swagger/OpenAPI.

## 📋 Informações do Projeto

- **Disciplina:** Desenvolvimento de APIs e Microserviços (DAM)
- **Integrantes:** Anna Julia Higa Farincho, Letícia Macedo, Evelyn Mercês
- **Grupo:** 4
- **Instituição:** IMPACTA

## 🚀 Funcionalidades

- **POST /users** - Criar novo usuário
- **GET /users** - Listar todos os usuários
- **GET /users/<id>** - Buscar usuário específico
- **PUT /users/<id>** - Atualizar usuário
- **DELETE /users/<id>** - Deletar usuário
- **GET /info** - Informações sobre a API

## 📚 Documentação Swagger

A API possui documentação automática gerada com Swagger/OpenAPI, acessível em:
- **Swagger UI:** http://localhost:5000/docs/
- **JSON OpenAPI:** http://localhost:5000/swagger.json

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask 2.3.3
- Flask-RESTX 1.3.0 (para Swagger)
- JSON para troca de dados
- HTTP Methods (GET, POST, PUT, DELETE)

## 📦 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/EveMerces/API-Simples-com-Flask.git
cd API-Simples-com-Flask
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**
```bash
python app.py
```

A API estará disponível em: http://localhost:5000

## 📖 Como usar a Documentação Swagger

1. **Acesse a documentação:** http://localhost:5000/docs/
2. **Explore os endpoints:** Todos os endpoints estão listados com descrições detalhadas
3. **Teste diretamente:** Use o botão "Try it out" para testar os endpoints
4. **Veja os modelos:** Schemas de request/response estão documentados
5. **Códigos de resposta:** Todos os códigos HTTP possíveis estão documentados

## 🔍 Testando a API

### Usando Swagger UI (Recomendado)
1. Acesse http://localhost:5000/docs/
2. Clique em qualquer endpoint
3. Clique em "Try it out"
4. Preencha os dados necessários
5. Clique em "Execute"

### Usando outras ferramentas
- **Postman** (recomendado para testes manuais)
- **cURL** (linha de comando)
- **Insomnia** (alternativa ao Postman)

## 📝 Exemplos de Uso

### Criar Usuário (POST /users)
```json
{
  "nome": "João Silva",
  "email": "joao.silva@email.com"
}
```

**Resposta (201 Created):**
```json
{
  "id": 4,
  "nome": "João Silva",
  "email": "joao.silva@email.com"
}
```

### Listar Usuários (GET /users)
**Resposta (200 OK):**
```json
[
  {
    "id": 1,
    "nome": "Anna Julia Higa Farincho",
    "email": "anna.julia@email.com"
  },
  {
    "id": 2,
    "nome": "Letícia Macedo",
    "email": "leticia.macedo@email.com"
  }
]
```

### Buscar Usuário Específico (GET /users/{id})
**Resposta (200 OK):**
```json
{
  "id": 1,
  "nome": "Anna Julia Higa Farincho",
  "email": "anna.julia@email.com"
}
```

## ⚠️ Observações Importantes

- **Armazenamento:** Os dados são armazenados em memória e serão perdidos quando a aplicação for reiniciada
- **IDs:** São gerados automaticamente de forma incremental
- **Validação:** A aplicação valida os dados de entrada e retorna códigos de status HTTP apropriados
- **Estrutura:** Projeto desenvolvido em um único arquivo `app.py` para simplicidade
- **Email único:** O sistema não permite emails duplicados

## 📊 Códigos de Status HTTP

- **200 OK** - Operação realizada com sucesso
- **201 Created** - Recurso criado com sucesso
- **400 Bad Request** - Dados inválidos ou malformados
- **404 Not Found** - Recurso não encontrado

## 🎯 Conceitos Implementados

Este projeto demonstra conceitos fundamentais de:
- APIs RESTful
- Framework Flask
- Operações CRUD
- Métodos HTTP
- Manipulação de JSON
- Status Codes HTTP
- **Documentação automática com Swagger/OpenAPI**
- **Validação de dados com Flask-RESTX**
- **Modelos de dados estruturados**
- **Organização de código com namespaces**

## 📈 Melhorias Implementadas

- ✅ Documentação automática com Swagger
- ✅ Validação robusta de dados
- ✅ Modelos de dados estruturados
- ✅ Mensagens de erro padronizadas
- ✅ Verificação de email único
- ✅ Interface interativa para testes
- ✅ Códigos de status HTTP apropriados
- ✅ Organização melhor do código

## 🔗 Links Úteis

- [Documentação Flask](https://flask.palletsprojects.com/)
- [Flask-RESTX Documentation](https://flask-restx.readthedocs.io/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)

---

**Desenvolvido com pelo Grupo 4 - IMPACTA**