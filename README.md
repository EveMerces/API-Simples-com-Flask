# 📁 Repositório: API-Simples-com-Flask

Este repositório contém duas atividades da disciplina **Desenvolvimento de APIs e Microserviços (DAM)**:

## 📂 Atividade 1: API-flask
API RESTful simples para gerenciamento de usuários com operações CRUD.

## 📂 Atividade 2: MVC-flask (Esta atividade)
Sistema web de gerenciamento de tarefas (To-Do List) desenvolvido com Flask seguindo a arquitetura MVC, permitindo que usuários criem, visualizem, editem e excluam tarefas.

---

# Gerenciador de Tarefas com Flask e MVC

**Disciplina:** Desenvolvimento de APIs e Microserviços (DAM)  
**Integrantes:** [Inserir nomes dos integrantes]  
**Grupo:** [Inserir número do grupo]  
**Instituição:** IMPACTA

## 🚀 Funcionalidades

- **Listar Tarefas:** Visualizar todas as tarefas cadastradas
- **Criar Tarefa:** Adicionar nova tarefa associada a um usuário
- **Atualizar Status:** Alternar status entre "Pendente" e "Concluído"
- **Excluir Tarefa:** Remover tarefa do sistema
- **Relacionamento:** Vinculação de tarefas a usuários existentes

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados
- **Jinja2** - Template engine
- **HTML/CSS** - Interface web
- **Arquitetura MVC** - Separação de responsabilidades

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/EveMerces/API-Simples-com-Flask.git
cd API-Simples-com-Flask
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação:**
```bash
python app.py
```

4. **Acesse no navegador:**
```
http://localhost:5000
```

## 🏗️ Estrutura do Projeto

```
projeto/
├── app.py                      # Arquivo principal com rotas
├── models/
│   ├── __init__.py
│   ├── user.py                 # Model de usuário (existente)
│   └── task.py                 # Model de tarefa (novo)
├── controllers/
│   ├── __init__.py
│   ├── user_controller.py      # Controller de usuário (existente)
│   └── task_controller.py      # Controller de tarefa (novo)
├── views/
│   └── templates/
│       ├── users.html          # Template de usuários (existente)
│       ├── tasks.html          # Template de listagem de tarefas (novo)
│       └── create_task.html    # Template de criação de tarefa (novo)
├── users.db                    # Banco de dados SQLite
└── requirements.txt
```

## 📊 Modelo de Dados

### Tabela Tasks
- **id** (Integer, PK) - Identificador único
- **title** (String, NOT NULL) - Título da tarefa
- **description** (String, NULL) - Descrição da tarefa
- **status** (String, NOT NULL, DEFAULT 'Pendente') - Status da tarefa
- **user_id** (Integer, FK) - Referência ao usuário

### Relacionamento
- **One-to-Many:** Um usuário pode ter várias tarefas
- **Foreign Key:** `tasks.user_id` → `users.id`

## 🌐 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tasks` | Lista todas as tarefas |
| GET | `/tasks/new` | Formulário para criar nova tarefa |
| POST | `/tasks/new` | Criar nova tarefa |
| POST | `/tasks/update/<int:task_id>` | Atualizar status da tarefa |
| POST | `/tasks/delete/<int:task_id>` | Excluir tarefa |

## 💻 Exemplos de Uso

### Criação de Tarefa
1. Acesse `/tasks/new`
2. Preencha o formulário:
   - **Título:** "Estudar Flask"
   - **Descrição:** "Revisar conceitos de MVC e SQLAlchemy"
   - **Usuário:** Selecione um usuário existente
3. Clique em "Criar Tarefa"

### Listagem de Tarefas
- Acesse `/tasks` para ver todas as tarefas
- Cada tarefa mostra: título, descrição, status e usuário responsável
- Botões disponíveis: "Concluir/Pendente" e "Excluir"

## 🏛️ Arquitetura MVC

### **Model** (`models/task.py`)
- Define a estrutura da tabela `tasks`
- Gerencia relacionamentos com a tabela `users`
- Implementa validações de dados

### **View** (`views/templates/`)
- **tasks.html:** Interface de listagem de tarefas
- **create_task.html:** Formulário de criação
- Utiliza Jinja2 para renderização dinâmica

### **Controller** (`controllers/task_controller.py`)
- **TaskController:** Classe com métodos estáticos
- Gerencia lógica de negócio
- Processa requisições entre View e Model

## 📝 Funcionalidades Implementadas

### ✅ CRUD Completo
- **Create:** Criar nova tarefa
- **Read:** Listar e visualizar tarefas
- **Update:** Atualizar status da tarefa
- **Delete:** Excluir tarefa

### ✅ Relacionamentos
- Relacionamento One-to-Many entre User e Task
- Chave estrangeira `user_id` na tabela tasks
- Consultas com JOIN para exibir nome do usuário

### ✅ Interface Web
- Templates HTML responsivos
- Formulários para entrada de dados
- Listagem organizada em tabela
- Botões de ação (Concluir/Excluir)

## 🎯 Conceitos Aplicados

Este projeto demonstra a implementação prática de:
- **Arquitetura MVC** - Separação de responsabilidades
- **ORM SQLAlchemy** - Mapeamento objeto-relacional
- **Relacionamentos de Banco** - Foreign Keys e JOINs
- **Template Engine** - Jinja2 para páginas dinâmicas
- **Operações CRUD** - Manipulação completa de dados
- **Framework Flask** - Desenvolvimento web em Python

## 📄 Observações

- **Banco de Dados:** Utiliza SQLite local (`users.db`)
- **Dados:** Tabela de usuários deve estar previamente populada
- **Status:** Tarefas alternam entre "Pendente" e "Concluído"
- **Arquitetura:** Seguimento rigoroso do padrão MVC

---

*Este projeto foi desenvolvido como atividade da disciplina Desenvolvimento de APIs e Microserviços (DAM) da IMPACTA, aplicando conceitos de arquitetura MVC, relacionamentos de banco de dados e desenvolvimento web com Flask.*