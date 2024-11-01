# Plano de Desenvolvimento Ágil (Scrum) para Sistema de Banco de Dados de Testes de Produção

## Objetivo Geral do Projeto
Desenvolver um sistema de banco de dados escalável e seguro para armazenar dados de testes de produção de dispositivos eletrônicos, com interface interativa para os usuários, armazenamento eficiente e automação de análises.

---

## 📅 Sprints e Entregáveis

### ✔️ Sprint 1: Configuração do Ambiente e Estrutura Inicial do Banco de Dados
**Objetivo:** Preparar a infraestrutura básica para o banco de dados e o ambiente de desenvolvimento.

- **User Stories:**
  - Como desenvolvedor, quero configurar um ambiente de desenvolvimento padronizado com Docker, para garantir consistência.
  - Como engenheiro de dados, quero definir e implementar as tabelas e relacionamentos iniciais em PostgreSQL, para que o banco de dados armazene dados estruturados.
- **Atividades:**
  - [ ] Configuração do ambiente Docker.
  - [ ] Configuração inicial do PostgreSQL com tabelas básicas.
- **Definição de Pronto:** Ambiente configurado com Docker e PostgreSQL inicializado com tabelas de dados de teste e primeiros relacionamentos.

---

### ⬜ Sprint 2: Conexão Backend e Estrutura Básica de API
**Objetivo:** Estabelecer a comunicação entre o banco de dados e a aplicação via API.

- **User Stories:**
  - Como desenvolvedor, quero criar uma API básica em Python para conectar com PostgreSQL, para realizar operações CRUD.
  - Como usuário, quero que a API me permita acessar e modificar registros no banco de dados.
- **Atividades:**
  - [ ] Implementação de endpoints CRUD para operações básicas de leitura e escrita.
  - [ ] Testes unitários para os endpoints principais.
- **Definição de Pronto:** API funcional com endpoints CRUD, conectada ao banco de dados PostgreSQL, com testes básicos de operação.

---

### ⬜ Sprint 3: Interface Inicial do Usuário (Frontend Angular)
**Objetivo:** Criar uma interface básica para interação com os dados do banco.

- **User Stories:**
  - Como usuário, quero visualizar registros armazenados no banco de dados em uma interface intuitiva.
  - Como usuário, quero acessar detalhes de um registro específico ao clicar na interface.
- **Atividades:**
  - [ ] Configuração do projeto Angular e integração com API.
  - [ ] Implementação de exibição de registros na interface.
- **Definição de Pronto:** Interface de usuário que exibe registros do banco de dados, com navegação funcional e design básico.

---

### ⬜ Sprint 4: Implementação de Filtragem e Ordenação de Dados
**Objetivo:** Melhorar a interface com opções de filtragem e ordenação dos registros.

- **User Stories:**
  - Como usuário, quero filtrar registros por critérios específicos, para visualizar apenas os dados relevantes.
  - Como usuário, quero ordenar os registros para facilitar a análise.
- **Atividades:**
  - [ ] Implementação de filtros e ordenação na API e no frontend.
  - [ ] Testes de filtragem e ordenação para garantir a precisão.
- **Definição de Pronto:** Filtros e ordenação implementados e funcionalidade verificada na interface.

---

### ⬜ Sprint 5: Segurança e Controle de Acesso
**Objetivo:** Assegurar que apenas usuários autorizados acessem o sistema e manipulem dados.

- **User Stories:**
  - Como usuário, quero fazer login para garantir que só pessoas autorizadas acessem o sistema.
  - Como administrador, quero definir permissões para restringir o acesso a dados e funcionalidades críticas.
- **Atividades:**
  - [ ] Implementação de autenticação e autorização (OAuth2 ou JWT).
  - [ ] Controle de acesso no backend para diferentes perfis de usuários.
- **Definição de Pronto:** Autenticação e controle de acesso implementados, com testes de segurança básicos concluídos.

---

### ⬜ Sprint 6: Automação de Análise de Dados e Relatórios
**Objetivo:** Criar scripts automáticos para análise dos dados armazenados, gerando relatórios periódicos.

- **User Stories:**
  - Como engenheiro de dados, quero automatizar a análise de dados para identificar tendências e métricas sem intervenção manual.
  - Como gerente de projeto, quero relatórios automáticos para acompanhar a qualidade e o desempenho dos dispositivos.
- **Atividades:**
  - [ ] Desenvolvimento de scripts de análise em Python para integração com o banco de dados.
  - [ ] Implementação de geração e armazenamento de relatórios.
- **Definição de Pronto:** Scripts de análise funcionando com agendamento periódico e relatórios armazenados para consulta.

---

### ⬜ Sprint 7: Testes Finais e Otimização do Sistema
**Objetivo:** Garantir que o sistema esteja otimizado para alto desempenho e pronto para a produção.

- **User Stories:**
  - Como engenheiro de dados, quero otimizar consultas e estrutura de banco de dados para suportar carga alta.
  - Como usuário final, quero que o sistema funcione de forma rápida e sem erros na produção.
- **Atividades:**
  - [ ] Testes de carga e stress no banco de dados e API.
  - [ ] Otimização de consultas e estrutura de dados.
- **Definição de Pronto:** Sistema validado com desempenho otimizado, pronto para implantação.

---

### 🔄 Status de Desenvolvimento

- [x] Sprint 1: Configuração do Ambiente e Estrutura Inicial do Banco de Dados
- [ ] Sprint 2: Conexão Backend e Estrutura Básica de API
- [ ] Sprint 3: Interface Inicial do Usuário (Frontend Angular)
- [ ] Sprint 4: Implementação de Filtragem e Ordenação de Dados
- [ ] Sprint 5: Segurança e Controle de Acesso
- [ ] Sprint 6: Automação de Análise de Dados e Relatórios
- [ ] Sprint 7: Testes Finais e Otimização do Sistema
