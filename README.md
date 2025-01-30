## **Documentação do Projeto de Agendamento de Consultas**

## Descrição Geral

Este projeto visa criar uma API de agendamento de consultas médicas utilizando **FastApi**. A API será usada para agendar, listar, editar e cancelar consultas, além de gerenciar médicos, pacientes e especialidades médicas.

### **Entidades Principais**

#### Paciente/Usuário
**Dados:**
- Nome
- CPF (único)
- Data de nascimento
- Telefone
- Email

**Funcionalidades:**
- Criar Paciente/Usuário
- Visualizar dados do Paciente
- Atualizar dados do Paciente
- Desativar Paciente

#### Médico
**Dados:**
- Nome
- CRM (único)
- Especialidade_id
- Telefone
- Email

**Funcionalidades:**
- Criar Médico
- Visualizar dados do Médico
- Atualizar dados do Médico
- Desativar Médico

#### Especialidade Médica
**Dados:**
- Nome da especialidade (ex. Cardiologia, Pediatria, etc.)
- Descrição

**Funcionalidades:**
- Criar Especialidade
- Listar Especialidades
- Editar Especialidade
- Desativar Especialidade

#### Consulta
**Dados:**
- IdPaciente (relacionado com a entidade Paciente)
- IdMedico (relacionado com a entidade Médico)
- IdEspecialidade (relacionado com a entidade Especialidade)
- Data e Hora da consulta
- Status (Agendada, Realizada, Cancelada)
- Observações

**Funcionalidades:**

- Agendar Consulta
- Listar Consultas de um Paciente
- Atualizar Consulta
- Cancelar Consulta

### Observações
**Todas as entidades devem conter:**
- Id
- Data de criação
- Data de atualização
- Status (Ativo/Inativo)

### **Estrutura de Rotas**
#### Pacientes
- **POST** `/pacientes` - Criar novo paciente
- **GET** `/pacientes/{id}` - Visualizar dados do paciente
- **PUT** `/pacientes/{id}` - Atualizar dados do paciente
- **PATCH** `/pacientes/{id}/desativar` - Desativar paciente

#### Médicos
- **POST** `/medicos` - Criar novo médico
- **GET** `/medicos/{id}` - Visualizar dados do médico
- **PUT** `/medicos/{id}` - Atualizar dados do médico
- **PATCH** `/medicos/{id}/desativar` - Desativar médico

#### Especialidades
- **POST** `/especialidades` - Criar nova especialidade
- **GET** `/especialidades` - Listar especialidades
- **PUT** `/especialidades/{id}` - Atualizar dados da especialidade
- **PATCH** `/medicos/{id}/desativar` - Desativar especialidade

#### Consultas
- **POST** `/consultas` - Agendar nova consulta
- **GET** `/consultas/paciente/{id}` - Listar consultas de um paciente
- **GET** `/consultas/{id}` - Detalhar uma consulta
- **PUT** `/consultas/{id}` - Atualizar consulta
- **PATCH** `/consultas/{id}/cancelar` - Cancelar consulta

### **Regras de Negócio e Validações**

#### Paciente
- O CPF deve ser único.
- O Email deve ser único.
- A data de nascimento deve ser validada.
- O paciente pode ser desativado, mas não excluído.

#### Médico
- O CRM deve ser único.
- O médico pode ser desativado, mas não excluído.
- O médico pode ter múltiplas especialidades associadas.

#### Especialidade
- Cada especialidade possui um nome único.
- O nome da especialidade deve ser preenchido corretamente.

#### Consulta
- O paciente e o médico devem ser válidos e associados a uma especialidade.
- A consulta não pode ser agendada para uma data e hora no passado.
- A consulta só pode ser cancelada antes da realização.
- As consultas devem ser agendadas com um intervalo mínimo (ex. 30 minutos) entre elas.

### **Tecnologias e Padrões**
- **API**: FastAPI, SqlAlchemy.
- **Banco de Dados**: Postgres.
- **Frontend**: Vue.js 3.
- **Infraestrutura**: Docker para containerização.
- **Autenticação**: JWT (JSON Web Tokens) para autenticação e autorização.
- **Validação de Dados**: Pydantic.
- **Testes**: Cobertura com testes unitários e de integração utilizando Pytest.

### **Próximos Passos**
- Finalizar a modelagem das entidades e diagramas de fluxo.
- Criar o projeto base.
- Implementar autenticação e autorização.
- Criar os endpoints incrementais para cada funcionalidade de CRUD.
- Desenvolver e testar os módulos de agendamento de consultas, gerenciamento de médicos, pacientes e especialidades.
- Implementar integração com a infraestrutura, como o envio de notificações de confirmação de consultas. 