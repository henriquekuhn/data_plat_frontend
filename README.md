# Plano de Desenvolvimento para Sistema de Banco de Dados de Testes de Produção

## Objetivo Geral do Projeto
Desenvolver um sistema de banco de dados escalável e seguro para armazenar dados de testes de produção de dispositivos eletrônicos, com interface interativa para os usuários, armazenamento eficiente e automação de análises.

---

## 📅 Sprints e Entregáveis

### Índice
1. [Sprint 1: Configuração do Ambiente e Estrutura Inicial do Banco de Dados](#1-sprint-1-configuração-do-ambiente-e-estrutura-inicial-do-banco-de-dados)

      1.1. [Passos para Configuração do Ambiente com Docker](#11-passos-para-configuração-do-ambiente-com-docker)

      1.2. [Configuração do PostgreSQL com Tabelas Básicas](#12-configuração-do-postgresql-com-tabelas-básicas)

      1.3. [Como Gerar um Backup do Container Docker](#13-como-gerar-um-backup-do-container-docker)

2. [Sprint 2: Desenvolvimento da API CRUD em Python com PostgreSQL](#2-sprint-2-desenvolvimento-da-api-crud-em-python-com-postgresql)

      2.1. [Implementação dos Endpoints CRUD](#21-implementação-dos-endpoints-crud)

      2.2. [Testes Unitários](#22-testes-unitários)

3. [Sprint 3: Interface Inicial do Usuário (Frontend Angular)](#3-sprint-3-interface-inicial-do-usuário-frontend-angular)
4. [Sprint 4: Implementação de Filtragem e Ordenação de Dados](#4-sprint-4-implementação-de-filtragem-e-ordenação-de-dados)
5. [Sprint 5: Segurança e Controle de Acesso](#5-sprint-5-segurança-e-controle-de-acesso)
6. [Sprint 6: Automação de Análise de Dados e Relatórios](#6-sprint-6-automação-de-análise-de-dados-e-relatórios)
7. [Sprint 7: Testes Finais e Otimização do Sistema](#7-sprint-7-testes-finais-e-otimização-do-sistema)


---

### ✔️ Sprint 1: Configuração do Ambiente e Estrutura Inicial do Banco de Dados
**Objetivo:** Preparar a infraestrutura básica para o banco de dados e o ambiente de desenvolvimento.

- **User Stories:**
  - Como desenvolvedor, quero configurar um ambiente de desenvolvimento padronizado com Docker, para garantir consistência.
  - Como engenheiro de dados, quero definir e implementar as tabelas e relacionamentos iniciais em PostgreSQL, para que o banco de dados armazene dados estruturados.
- **Atividades:**
  - [x] Configuração do ambiente Docker.
  - [x] Configuração inicial do PostgreSQL com tabelas básicas.
- **Definição de Pronto:** Ambiente configurado com Docker e PostgreSQL inicializado com tabelas de dados de teste e primeiros relacionamentos.
  
Status: **Concluída**

---

### ✔️ Sprint 2: Conexão Backend e Estrutura Básica de API (Em Andamento)
**Objetivo:** Estabelecer a comunicação entre o banco de dados e a aplicação via API.

- **User Stories:**
  - Como desenvolvedor, quero criar uma API básica em Python para conectar com PostgreSQL, para realizar operações CRUD.
  - Como usuário, quero que a API me permita acessar e modificar registros no banco de dados.
- **Atividades:**
  - [ ] Implementação de endpoints CRUD para operações básicas de leitura e escrita.
  - [ ] Testes unitários para os endpoints principais.
- **Definição de Pronto:** API funcional com endpoints CRUD, conectada ao banco de dados PostgreSQL, com testes básicos de operação.

Status: **Concluída**

---

### ⬛ Sprint 3: Data Scrapping
**Objetivo:** Desenvolver algorítmo para realizar coleta de dados de relátórios de teste.

- **User Stories:**
  - Como desenvolvedor, quero criar uma API básica em Python para, utilizando os comandos CRUD, realizar o scrapping de dados de relatorios de teste já efetuados.
  - Como usuário, quero que a API me permita gerar tabelas em um banco de dados com os dados do relatório.
- **Atividades:**
  - [ ] Implementação de algoritmo para leitura de dados de PDF.
  - [ ] Implementação de algoritmo para criação de tabelas e escrita de dados.
  - [ ] Testes unitários para o algoritmo.
- **Definição de Pronto:** Código pronto e testado, com o banco de dados e suas tabelas criadas e preenchidas com os arquivos dispostos.

Status: **Concluída**

---

### ⬛ Sprint 3: Interface Inicial do Usuário (Frontend Angular)
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

## 🔄 Status de Desenvolvimento

- [x] Sprint 1: Configuração do Ambiente e Estrutura Inicial do Banco de Dados (Concluída)
- [x] Sprint 2: Conexão Backend e Estrutura Básica de API (Em Andamento)
- [ ] Sprint 3: Interface Inicial do Usuário (Frontend Angular)
- [ ] Sprint 4: Implementação de Filtragem e Ordenação de Dados
- [ ] Sprint 5: Segurança e Controle de Acesso
- [ ] Sprint 6: Automação de Análise de Dados e Relatórios
- [ ] Sprint 7: Testes Finais e Otimização do Sistema

---

# 1. Sprint 1: Configuração do Ambiente e Estrutura Inicial do Banco de Dados

## User Stories
1. **Como desenvolvedor**, quero configurar um ambiente de desenvolvimento padronizado com Docker, para garantir consistência entre as etapas de desenvolvimento e produção.
2. **Como engenheiro de dados**, quero definir e implementar as tabelas e relacionamentos iniciais em PostgreSQL, para que o banco de dados armazene dados estruturados.

---

## Tarefas e Atividades

### 1.1 Configuração do Ambiente com Docker
- **Atividade:** Instalar Docker no ambiente local (se necessário) e criar contêineres para PostgreSQL e demais serviços essenciais.
- **Critérios de Aceitação:** Docker instalado, contêineres criados com Docker Compose, rodando de forma consistente no ambiente de desenvolvimento.
- **Status de Pronto:** Ambiente local executando PostgreSQL em um contêiner Docker.

### 1.2 Configuração do PostgreSQL com Tabelas Básicas
- **Atividade:** Estruturar e implementar tabelas iniciais para o armazenamento de dados de teste, incluindo valores, resultados e limites, usando SQL.
- **Critérios de Aceitação:** Tabelas básicas criadas com os tipos de dados definidos; relacionamentos principais implementados e funcionando.
- **Status de Pronto:** Banco de dados PostgreSQL populado com a estrutura inicial de tabelas e com dados de teste.

### 1.3 Documentação do Ambiente e Configuração do Banco
- **Atividade:** Documentar os passos para instalação, configuração do Docker e criação das tabelas iniciais no banco de dados.
- **Critérios de Aceitação:** Documentação clara e detalhada, com instruções para reprodução do ambiente e detalhes das tabelas.
- **Status de Pronto:** Documentação completa e acessível a todos os desenvolvedores para assegurar a reprodutibilidade.

---

## Definição de Pronto
Para a Sprint 1 ser considerada completa:
- O ambiente de desenvolvimento deve estar configurado com Docker, rodando PostgreSQL em um contêiner.
- As tabelas iniciais e relacionamentos do banco de dados devem estar criados e testados.
- Documentação do ambiente e banco de dados disponível para a equipe.

Essa estrutura para a Sprint 1 permitirá uma base sólida para o desenvolvimento do sistema, facilitando o trabalho nas sprints seguintes.

---

## 1.1. Passos para Configuração do Ambiente com Docker

### Instalação do Docker
1. **Baixe e Instale o Docker:**
   - Acesse Docker Desktop e baixe a versão para seu sistema operacional.
   - Siga as instruções de instalação para configurar o Docker em sua máquina.

2. **Verifique a Instalação:**
   - Abra um terminal (Prompt de Comando ou PowerShell no Windows).
   - Execute o comando:
     ```bash
     docker --version
     ```
   - Isso deve exibir a versão do Docker instalada.

### Criação do Arquivo `docker-compose.yml`
1. **Crie um diretório para o projeto:**
   ```bash
   mkdir data-plat
   cd data-plat
   ```
   
2. Criação do Arquivo `docker-compose.yml`

  - Abra um editor de texto e adicione o seguinte conteúdo:

```yaml
services:
  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: cafrunikuhn
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: data_plat
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## 1.2. Configuração do PostgreSQL com Tabelas Básicas
   
### Iniciar o Contêiner

1. **Inicie o contêiner com Docker Compose:**

-	No terminal, dentro do diretório do projeto, execute:
 ``` 
docker-compose up -d
```
-	O parâmetro -d inicia o contêiner em modo destacado (em segundo plano).

2.	**Verifique se o contêiner está em execução:**
-	Use o comando:
```
docker ps
```
-	Você deve ver o contêiner listado como data-plat-db-1.

### Acessar o Banco de Dados

1.	**Acesse o contêiner PostgreSQL:**
Execute o seguinte comando para abrir o cliente psql:
```
docker exec -it data-plat-db-1 psql -U cafrunikuhn -d data_plat
```
### Verificar Persistência dos Dados

1.	**Crie uma tabela e insira dados:**
```
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO test_table (name) VALUES ('Test Data 1'), ('Test Data 2');
```

2.	**Verifique os dados inseridos:**
```
SELECT * FROM test_table;
```
4.	**Pare o contêiner:**
```
docker-compose down
```
6.	**Reinicie o contêiner:**
```
docker-compose up -d
```
8.	**Acesse novamente o contêiner:**
```
docker exec -it data-plat-db-1 psql -U cafrunikuhn -d data_plat
```
10.	**Verifique se os dados ainda estão presentes:**
```
SELECT * FROM test_table;
```
### Debug do Contêiner (Opcional)
Se você precisar depurar o contêiner, use o seguinte comando:
```
docker debug data-plat-db-1
```

### Guia Rápido
Este guia fornece instruções detalhadas para:

1.	Listar tabelas no PostgreSQL dentro de um contêiner Docker.
2.	Excluir tabelas específicas.
3.	Comandos SQL para manipulação de tabelas.

________________________________________
1. Listando Tabelas no Banco de Dados PostgreSQL

Para listar as tabelas de um banco de dados específico dentro do contêiner Docker, siga os passos abaixo:

Passo 1: Acessar o Banco de Dados PostgreSQL

Execute o comando abaixo no terminal para entrar no contêiner e acessar o banco de dados data_plat:

```
docker exec -it data-plat-db-1 psql -U cafrunikuhn -d data_plat
```

•	docker exec -it: Executa um comando interativo no contêiner.

•	data-plat-db-1: Nome do contêiner Docker.

•	psql -U cafrunikuhn -d data_plat: Comando para abrir o prompt psql do PostgreSQL com o usuário e banco de dados especificados.

Passo 2: Listar as Tabelas Existentes

No prompt do PostgreSQL, execute o comando para listar todas as tabelas:

```
\dt
```

Esse comando exibe uma lista de todas as tabelas no banco de dados data_plat.

Passo 3: Sair do Prompt do PostgreSQL

Para sair do prompt, basta digitar:

```
\q
```
________________________________________
2. Excluindo Tabelas no PostgreSQL

Para remover uma tabela específica do banco de dados PostgreSQL, siga as instruções abaixo.

Passo 1: Acessar o Banco de Dados PostgreSQL

No terminal, acesse o contêiner e o banco de dados da mesma forma:

```
docker exec -it data-plat-db-1 psql -U cafrunikuhn -d data_plat
```
Passo 2: Executar o Comando para Excluir a Tabela

No prompt do PostgreSQL, execute o comando DROP TABLE para excluir a tabela desejada. Substitua nome_da_tabela pelo nome da tabela que você deseja excluir.

```
DROP TABLE nome_da_tabela;
```

Observação

Se quiser excluir a tabela apenas se ela existir, evitando erros caso a tabela não esteja presente, use o seguinte comando:

DROP TABLE IF EXISTS nome_da_tabela;

<span style="color:red">Este comando exclui a tabela e todos os dados nela de forma permanente.</span>  

Passo 3: Sair do Prompt do PostgreSQL

Para finalizar, digite o comando para sair do prompt:

```
\q
```
________________________________________
Resumo dos Comandos Utilizados

| Comando                                    | Função                                         |
|--------------------------------------------|------------------------------------------------|
| `docker exec -it <container> psql -U <user> -d <db>` | Acessa o banco de dados PostgreSQL no contêiner Docker |
| `\dt`                                      | Lista todas as tabelas do banco de dados       |
| `DROP TABLE nome_da_tabela;`               | Exclui uma tabela específica                   |
| `DROP TABLE IF EXISTS nome_da_tabela;`     | Exclui uma tabela apenas se ela existir        |
| `\q`                                       | Sai do prompt do PostgreSQL                    |


### Conclusão

Este guia deve ajudá-lo a gerenciar as tabelas em um banco de dados PostgreSQL em contêineres Docker de maneira segura e eficiente.

Resumo dos Comandos Utilizados
Comando	Função
docker exec -it <container> psql -U <user> -d <db>	Acessa o banco de dados PostgreSQL no contêiner Docker
\dt	Lista todas as tabelas do banco de dados
DROP TABLE nome_da_tabela;	Exclui uma tabela específica
DROP TABLE IF EXISTS nome_da_tabela;	Exclui uma tabela apenas se ela existir
\q	Sai do prompt do PostgreSQL
Este guia deve ajudá-lo a gerenciar as tabelas em um banco de dados PostgreSQL em contêineres Docker de maneira segura e eficiente.

## Gerando banco de dados através de arquivo SQL:

1. Crie um arquivo chamado `sprint1_test_table.sql` em seu diretório de projeto com o seguinte conteúdo:

```
CREATE TABLE dut_completo (
    id SERIAL PRIMARY KEY,
    lot VARCHAR(50),
    version VARCHAR(50),
    date DATE
);

CREATE TABLE teste (
    id SERIAL PRIMARY KEY,
    dut_id INT NOT NULL,
    test_name VARCHAR(255) NOT NULL,  -- Ex.: "Continuidade", "Leakage"
    pin INT,
    temperature DECIMAL(5,2),
    voltage DECIMAL(5,2),
    result VARCHAR(255),  
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dut_id) REFERENCES dut_completo(id) ON DELETE CASCADE
);
```

2. Executar o Arquivo SQL no PostgreSQL:

Para executar o arquivo SQL e criar os bancos de dados e as tabelas, siga os passos abaixo:

Passo 1: Acesse o Contêiner PostgreSQL
No terminal, acesse o contêiner do PostgreSQL:

```
docker exec -it data-plat-db-1 psql -U your_user
```

Passo 2: Execute o Arquivo SQL
Com o prompt do PostgreSQL aberto, execute o arquivo SQL com o seguinte comando:

```
\i /path/to/your/sprint1_test_table.sql
```

Substitua /path/to/your/setup.sql pelo caminho real onde você salvou o arquivo sprint1_test_table.sql dentro do contêiner. Você pode precisar copiar o arquivo para o contêiner ou montá-lo como um volume no Docker.

3. Verificar a Criação das Tabelas:

Após executar o arquivo SQL, você pode verificar se as tabelas foram criadas corretamente usando o comando:

```
\dt
```

Isso exibirá uma lista de todas as tabelas no banco de dados data_plat.

## 1.3. Como Gerar um Backup do Container Docker

### 1. Identifique o Container ID

Para criar um backup, você primeiro precisa identificar o ID do container. Abra o terminal e execute o comando:

```
docker ps -a
```

Este comando lista todos os containers, incluindo os que estão parados. A saída será algo assim:

```
CONTAINER ID   IMAGE             COMMAND                  CREATED      STATUS                          PORTS     NAMES
966bd5b967d2   postgres:latest   "docker-entrypoint.s…"   6 days ago   Exited (0) About a minute ago             data-plat-db-1
```

O CONTAINER ID do container que queremos é, neste exemplo, 966bd5b967d2. Anote esse ID para usá-lo no próximo passo.

### 2. Execute o Comando de Exportação

Agora que você tem o ID, você pode exportar o container. No terminal, use o seguinte comando:

```
docker export <CONTAINER_ID> > container_backup.tar
```

Substitua <CONTAINER_ID> pelo ID do container que você anotou. No exemplo anterior, o comando seria:

```
docker export 966bd5b967d2 > container_backup.tar
```

Esse comando cria um arquivo chamado container_backup.tar no diretório atual. Este arquivo contém o sistema de arquivos do container em um formato que pode ser importado em outra instância do Docker.

### 3. Verifique o Backup

Após a exportação, você verá o arquivo container_backup.tar no diretório onde o comando foi executado. Este arquivo pode ser movido para outro computador ou mantido como backup.

### 4. Como Restaurar o Backup em Outro Ambiente

Quando precisar restaurar o backup, você pode usar o comando docker import. Aqui está como fazer isso:

```
docker import container_backup.tar new_container_image
```

Isso cria uma nova imagem chamada new_container_image a partir do backup. Você pode então criar um novo container a partir dessa imagem usando o comando:

```
docker run -d --name restored_container new_container_image
```

Isso inicia o container restaurado em segundo plano.



# 2. Sprint 2: Desenvolvimento da API CRUD em Python com PostgreSQL

## User Stories

1. **Como desenvolvedor**, quero criar uma API básica em Python que conecte ao PostgreSQL para realizar operações CRUD.

2. **Como usuário**, quero que a API permita acessar e modificar registros no banco de dados de forma segura e estruturada.

## Tarefas e Atividades

### 2.1 Implementação dos Endpoints CRUD para Operações Básicas

- Atividade: Desenvolver uma API que suporte as operações CRUD (Create, Read, Update, Delete) para permitir a interação com o banco de dados.

- Critérios de Aceitação: Endpoints funcionando para criar, ler, atualizar e deletar registros, com parâmetros flexíveis para operar em qualquer tabela.

- Status de Pronto: API conectada ao PostgreSQL com endpoints CRUD operacionais.

### 2.2 Implementação de Testes Unitários para os Endpoints

- Atividade: Criar testes unitários para cada operação CRUD da API, garantindo seu funcionamento correto e identificando possíveis erros.

- Critérios de Aceitação: Testes para todos os endpoints desenvolvidos, cobrindo as operações de criação, leitura, atualização e exclusão.

- Status de Pronto: Testes executados com sucesso diretamente no VSCode, validando a funcionalidade dos endpoints.

### 2.3 Documentação da API e dos Endpoints CRUD

- Atividade: Documentar o funcionamento da API, explicando o código, descrevendo cada função, e fornecendo instruções de uso.

- Critérios de Aceitação: Documentação clara e acessível, com tabela de funções, explicação das operações CRUD, e sugestões de melhorias futuras.

- Status de Pronto: Documentação completa com exemplos de uso e orientações de como aprimorar o projeto.

## Definição de Pronto
Para a Sprint 2 ser considerada completa:

- A API deve estar funcional com endpoints CRUD conectados ao banco de dados PostgreSQL.

- Todos os testes unitários básicos para CRUD devem estar implementados e executados com sucesso.

- A documentação da API, endpoints e orientações de melhorias deve estar finalizada e disponível para a equipe.


## 2.1. Implementação dos Endpoints CRUD

### Estrutura do Código:

main.py: Contém a classe DatabaseConnection, que implementa os métodos de conexão e operações CRUD.

crud_test.py: Arquivo de testes unitários para cada função da API, com validação de funcionamento.

#### Funções CRUD:

| Função         | Descrição                                                                                   | Parâmetros                                                                                 | Retorno                           |
|----------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------|
| `connect`      | Estabelece conexão com o banco de dados.                                                    | Nenhum                                                                                     | `True` se conectado, caso contrário `False` |
| `create_table` | Cria uma tabela com um `id` (chave primária) e `created_at` (timestamp).                    | `table_name` (string)                                                                      | `True` se sucesso, caso contrário `False` |
| `add_columns`  | Adiciona colunas a uma tabela existente.                                                    | `table_name` (string), `columns` (dicionário de colunas e tipos, ex: `{"coluna": "tipo"}`) | `True` se sucesso, caso contrário `False` |
| `add_data`     | Insere dados em colunas da tabela.                                                          | `table_name` (string), `column_data` (lista de dicionários)                                | `True` se sucesso, caso contrário `False` |
| `delete_data`  | Exclui dados de uma tabela com base em uma condição.                                        | `table_name` (string), `reference`, `data`                                                 | `True` se sucesso, caso contrário `False` |
| `update_data`  | Atualiza dados de uma coluna com base em condições.                                         | `table_name`, `update_column`, `new_value`, `reference_column_and_value`                   | `True` se sucesso, caso contrário `False` |


## 2.2. Testes Unitários

Para executar os testes, utilize o arquivo crud_test.py. O arquivo inclui testes para:

- Conexão com o Banco de Dados: Valida a conexão com o PostgreSQL.

- CRUD Completo: Verifica se cada operação CRUD está funcional e com retorno esperado.

- Persistência de Dados: Testa a persistência ao inserir, atualizar e deletar registros em tabelas específicas.

| Função             | Descrição                                                                                  | Parâmetros                                   | Retorno Esperado                                          |
|--------------------|--------------------------------------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------|
| test_connect       | Testa a função de conexão com o banco de dados.                                             | Nenhum                                       | `True` se a conexão for bem-sucedida, `False` caso contrário|
| test_create_table  | Testa a criação de uma tabela no banco de dados.                                            | `table_name` (nome da tabela)                | `True` se a tabela for criada com sucesso, `False` caso contrário|
| test_add_columns   | Testa a adição de novas colunas a uma tabela existente.                                     | `table_name` (nome da tabela), `columns` (dicionário de colunas e tipos) | `True` se as colunas forem adicionadas com sucesso, `False` caso contrário|
| test_add_data      | Testa a inserção de dados em uma tabela.                                                   | `table_name` (nome da tabela), `column_data` (lista de dicionários) | `True` se os dados forem inseridos com sucesso, `False` caso contrário|
| test_delete_data   | Testa a exclusão de dados de uma tabela com base em uma condição.                          | `table_name` (nome da tabela), `reference` (coluna de referência), `data` (dados) | `Número de registros excluídos` |
| test_update_data   | Testa a atualização de dados de uma tabela com base em uma condição.                       | `table_name` (nome da tabela), `update_column` (coluna a ser atualizada), `new_value` (novo valor), `reference_column_and_value` (condição de atualização) | `True` se a atualização for bem-sucedida, `False` caso contrário|

#### Como Rodar os Testes:

1. Inicie o servidor PostgreSQL e configure o banco de dados de acordo com os parâmetros definidos.

2. Execute os testes com o comando:

```
pytest back/unittest/crud_test.py
```

## 2.3. Sugestões de Melhorias

- Adicionar a implementação em Docker

- Aplicar conceito SMART

- Autenticação e Segurança: Implementar autenticação para proteger os endpoints e limitar o acesso.

- Validação de Dados: Adicionar verificações de tipos e formato de dados para cada entrada no banco de dados.

- Tratamento de Erros: Aprimorar o tratamento de erros com mensagens de retorno mais específicas.

- Documentação Automática: Utilizar ferramentas como Swagger para gerar documentação interativa dos endpoints.


## Conclusão

Esta Sprint forneceu a base de uma API CRUD em Python para PostgreSQL, permitindo interações fundamentais com o banco de dados. As melhorias sugeridas orientam o avanço para uma API mais segura e robusta.


# 3. Sprint 3: Data Scrapping

## User Stories

1. Como um desenvolvedor, quero criar um banco de dados SQL utilizando MariaDB e Python para armazenar resultados de testes, de forma que os dados sejam acessíveis e consultáveis por meio de uma interface.

2. Como um engenheiro, desejo validar o armazenamento de dados usando testes unitários com MariaDB e SQLite, para garantir a correção e a integridade do sistema.

3. Como um usuário, quero visualizar os resultados atraves de um terminal iterativo

## Tarefas e Atividades

1. Planejamento das tabelas:
   - Definir os relatórios PDF que serão utilizados.
   - Definir as tabelas que serão criadas.
   - Definir a estrutura das tabelas.

2. Data Scrapping:
   - Desenvolver algoritmo para leitura de pdf.
   - Estruturar dados lidos.

3. Desenvolver o banco de dados:
   - Criar as tabelas necessárias usando SQLAlchemy.
   - Implementar conexão entre o banco de dados e a aplicação.
   - Armazenar dados nas tabelas

3. Implementar funcionalidades:
   - Criar comandos para iteração com as tabelas.

4. Teste de implementação
   - Desenvolver testes unitários para validar as operações de CRUD no banco de dados.
   - Validar srapping e registro dos dados.

5. Criar a interface do usuário:
   - Desenvolver uma interface básica para interação pelo terminal.

6. Documentar o processo:
   - Gerar uma documentação detalhada contendo configurações, código e explicações.

## Definição de Pronto (DoD)

1. Definição da estrutura das tabelas.
2. Coleta de dados dos relatórios funcionando.
3. Organização do dados funcionando corretamente.
4. Criação das tabelas e armazenamento dos dados.
5. Teste de validação cruzada entre relatórios e banco de dados
6. Documentação técnica completa foi gerada.


### 3.1 Planejamento das tabelas.

### Tabela: `yield_platform`

Esta tabela armazena dados relacionados aos testes realizados em plataformas de testes, incluindo parâmetros, resultados e validações associadas.

| **Coluna**         | **Tipo de Dado** | **Descrição**                                                                                           | **Exemplo**                        |
|--------------------|------------------|---------------------------------------------------------------------------------------------------------|------------------------------------|
| `id`               | `INT`            | Identificador único de cada registro na tabela.                                                          | `1`               |
| `created_at`       | `DATETIME`       | Data e hora em que o teste foi registrado.                                                               | `2024-11-28 19:52:27.866601`      |
| `dut_id`           | `INT`            | Identificador do dispositivo sob teste (DUT - Device Under Test).                                        | `123`                                |
| `test_type`        | `VARCHAR(50)`    | Tipo de teste realizado.                                                                                 | `maximum_output`, `evm`, `frequency error` |
| `pin_name`         | `VARCHAR(50)`    | Nome do pino de teste, se aplicável.                                                                      | `03@00`, `28`               |
| `flash_step`       | `VARCHAR(50)`    | Passo do flash, se aplicável.                                                                             | `01`                   |
| `peripheral_id`    | `VARCHAR(50)`    | Identificador do periférico testado, se aplicável.                                                       | `28`                   |
| `sleep_mode`       | `VARCHAR(50)`    | Sleep Mode, se aplicável.                                                                                | `SLEEP2`                            |
| `calibration_id`   | `VARCHAR(50)`    | Identificador da calibração, se aplicável.                                                                |`AFC`                             |
| `band`             | `VARCHAR(50)`    | Banda de frequência utilizada no teste.                                                                   | `08`, `28`, `03`                  |
| `frequency`        | `FLOAT`          | Valor da frequência medida durante o teste.                                                               | `897.5`, `725.5`, `836.5`         |
| `test_item`        | `VARCHAR(50)`    | Identificador do item de teste.                                                                           | `03@00`, `00@00`, `03@00`         |
| `di_channel`       | `VARCHAR(50)`    | Canal de entrada do dispositivo de teste, se aplicável.                                                   | `3625`                             |
| `cell_level`       | `FLOAT`          | Nível de célula medido durante o teste.                                                                   | `19.8`, `17.5`, `167.3`           |
| `lower_limit`      | `FLOAT`          | Limite inferior do valor esperado para o teste.                                                           | `22.3`, `17.5`, `174.75`          |
| `uper_limit`       | `FLOAT`          | Limite superior do valor esperado para o teste.                                                           | `21.8`, `3.0`, `8.96`             |
| `result`           | `VARCHAR(10)`    | Resultado do teste: "PASS" ou "FAIL".                                                                     | `PASS`, `PASS`, `PASS`            |
| `unit`             | `VARCHAR(10)`    | Unidade de medida do valor testado.                                                                      | `dBm`, `%`, `Hz`                  |
| `judgement`        | `VARCHAR(10)`    | Julgamento final do teste.    

## Exemplo de consulta

```sql
SELECT * FROM yield_platform WHERE test_type = 'short open' AND result = 'PASS';
```

Este exemplo retorna todos os registros de testes do tipo "short open" que passaram com sucesso.

- As colunas created_at, id e test_type são essenciais para o monitoramento e rastreamento histórico dos testes.
- A coluna result é fundamental para determinar se o teste foi bem-sucedido ou falhou, de acordo com os critérios estabelecidos.


### Tabela: `dut_register`

Esta tabela armazena informações relacionadas ao registro de dispositivos sob teste (DUT - Device Under Test) e ao histórico dos testes realizados, incluindo detalhes sobre os lotes, operadores e tempo total de teste.

| **Coluna**          | **Tipo de dado**    | **Descrição**                                                                                  | **Exemplo**               |
|---------------------|---------------------|------------------------------------------------------------------------------------------------|---------------------------|
| `id`                | `INT`               | Identificador único de cada registro na tabela.                                                 | `1`             |
| `created_at`        | `DATETIME`          | Data e hora em que o registro foi criado.                                                      | `2024-12-10 14:30:00`     |
| `dut_id`            | `INT`               | Identificador único do dispositivo sob teste (DUT - Device Under Test).                        | `123`            |
| `operator`          | `VARCHAR(50)`       | Nome do operador responsável pela execução do teste.                                           | `Operador A`, `Operador B`|
| `batch`             | `VARCHAR(50)`       | Identificador do lote de dispositivos testados.                                                | `Batch001`, `Batch002`    |
| `start_time`        | `DATETIME`          | Data e hora de início do teste.                                                                | `2024-12-10 08:00:00`     |
| `total_time`        | `FLOAT`             | Tempo total gasto no teste, em minutos.                                                        | `120.5`, `150.0`          |
| `test_plan`         | `VARCHAR(100)`      | Plano de teste associado ao DUT, descrevendo os testes realizados.                             | `Test Plan A`, `Test Plan B` |
| `plat_sw_v`         | `VARCHAR(20)`       | Versão do software da plataforma de teste utilizada.                                           | `v1.2.3`, `v2.0.1`        |
| `plat_hw_v`         | `VARCHAR(20)`       | Versão do hardware da plataforma de teste utilizada.                                           | `v1.1`, `v2.0`            |
| `n_test_items`      | `INT`               | Número total de itens de teste no plano de teste.                                              | `10`, `20`                |
| `n_pass_items`      | `INT`               | Número de itens de teste que passaram no teste.                                                | `8`, `15`                 |

## Exemplo de consulta

```sql
SELECT * FROM dut_register WHERE batch = ' NB2PT07-02-1' AND start_time = '08/27/2024';
```

- A coluna created_at fornece o timestamp do registro, sendo importante para o controle histórico dos testes.
- A coluna start_time e total_time ajudam a monitorar o tempo gasto para concluir o teste de cada DUT.
- As colunas n_test_items e n_pass_items são cruciais para determinar a eficiência do teste, representando respectivamente o número total de itens testados e o número de itens que passaram no teste.

### 3.2 Data Scrapping (text_from_pdf.py)

#### 3.2.1 Bibliotecas Importadas:

O código usa `pdfplumber` para extração de dados de PDFs, `re` para expressões regulares e `os` para manipulação de arquivos e diretórios.

Ele também importa uma classe `DatabaseConnection` de um módulo `main`, que lida com a conexão ao banco de dados.

#### 3.2.2 Overview do Código

#### Função count_pdfs_in_directory:

Essa função percorre um diretório e conta o número de arquivos PDF nele, o que pode ser útil para saber quantos PDFs precisam ser processados.
Dicionários e Tabelas de Dados:

O código tem uma estrutura de dicionários chamada PATTERNS, onde cada chave representa um tipo de teste e o valor é uma lista com dois elementos: o número de linhas de dados no PDF e o nome da função que irá processar esse teste (por exemplo, create_dut, create_shortopen).

A lista TABLES contém os nomes das tabelas do banco de dados onde os dados serão armazenados: `dut_register` e `yield_platform`'.

A variável `COLUMNS` define os esquemas de duas tabelas, com os nomes das colunas e seus tipos.

#### Funções de Criação de Dados:

Cada função de criação de dados (como create_dut, create_shortopen, etc.) processa um tipo de teste específico, extraindo as informações do PDF com base em um padrão de expressão regular.

Para cada teste, as informações extraídas são inseridas nas tabelas do banco de dados usando `db.add_data()`, embora o objeto db não tenha sido mostrado no código.

#### Expressões Regulares:

Cada função de criação de dados usa uma expressão regular (re.match) para capturar as colunas dos dados do teste a partir do texto do PDF.

As expressões regulares são projetadas para corresponder ao formato específico dos dados de cada tipo de teste. No entanto, você deve garantir que os padrões sejam compatíveis com os dados reais no seu arquivo PDF.

### 3.3 Desenvolver o banco de dados: (db_operation.py)

O código interage com um banco de dados PostgreSQL utilizando SQLAlchemy, que é uma biblioteca de mapeamento objeto-relacional (ORM) e também permite execução de consultas SQL de forma eficiente. Abaixo, explico detalhadamente como o processo de registro e consulta de dados foi implementado no código.


#### 3.3.1 Conexão com o Banco de Dados

- `create_engine(DATABASE_URL)`: A conexão com o banco de dados é estabelecida utilizando a função create_engine do SQLAlchemy. A URL de conexão inclui o tipo de banco de dados `(postgresql+psycopg2)`, o nome de usuário, a senha, o host e o nome do banco de dados:

```python
DATABASE_URL = "postgresql+psycopg2://cafrunikuhn:admin@localhost/data_plat"
engine = create_engine(DATABASE_URL)
```

- O `engine` é a principal interface para interação com o banco de dados, permitindo enviar consultas SQL e manipular os dados.

#### 3.3.2 Reflexão das Tabelas:

`MetaData()`: A classe MetaData é usada para refletir as tabelas existentes no banco de dados. A reflexão permite que o SQLAlchemy automaticamente busque a estrutura das tabelas já criadas no banco, sem que o desenvolvedor precise definir manualmente os modelos.

```python
metadata = MetaData()
metadata.reflect(bind=engine)
```

`metadata.tables['dut_register']` e `metadata.tables['yield_platform']`: Após a reflexão, o SQLAlchemy mapeia as tabelas dut_register e yield_platform no banco, e essas tabelas são acessadas através de metadata.tables.

#### 3.3.3 Consultas ao Banco de Dados:
Consulta com Filtro (Filtro por batch):

A função list_column_values é usada para listar os valores distintos de uma coluna (batch, neste caso) em uma tabela. Isso é útil para fornecer ao usuário opções de filtro para consulta.

Quando o usuário escolhe o filtro por batch, os valores dessa coluna são exibidos, e o usuário pode selecionar um para filtrar os resultados. O valor selecionado é então passado para a função `query_data`.

```python
batches = list_column_values(engine, dut_register_table, "batch")
```

#### Execução da Consulta:

`select(dut_register_table)`: A consulta SQL para a tabela dut_register é construída utilizando a função `select()` do SQLAlchemy. O filtro é aplicado se o valor do filtro (filter_value) for fornecido. Caso contrário, a consulta retorna todos os registros.

```python
dut_register_query = select(dut_register_table).where(dut_register_table.c[filter_column] == filter_value)
```

`select(yield_platform_table)`: Após filtrar a tabela dut_register, os dut_id correspondentes são usados para realizar uma consulta na tabela yield_platform.

O SQLAlchemy cria a consulta para selecionar os registros de yield_platform que possuem os `dut_id` filtrados da tabela `Dut_register`.

```python
yield_platform_query = select(yield_platform_table).where(yield_platform_table.c.dut_id.in_(dut_ids))
```

#### 3.3.4 Execução da Consulta SQL:

O método `connection.execute()` é utilizado para executar a consulta construída. Ele retorna os resultados da consulta, que são então processados e exibidos para o usuário.

```python
dut_register_result = connection.execute(dut_register_query)
yield_platform_result = connection.execute(yield_platform_query)
```

#### Resultado da Consulta:

`fetchall()` é chamado para recuperar todos os resultados da consulta. O método retorna os dados, que podem ser iterados e exibidos para o usuário.

```python
dut_register_rows = dut_register_result.fetchall()
yield_platform_rows = yield_platform_result.fetchall()
```

#### 3.3.5 Execução sem Filtro:

Se o usuário escolher não aplicar nenhum filtro, a consulta à tabela yield_platform é feita sem nenhum critério de filtro:

```python
yield_platform_query = select(yield_platform_table)
yield_platform_result = connection.execute(yield_platform_query)
```

#### Função `query_data`:

A função query_data é responsável por realizar a consulta, filtrar os dados com base no filter_column e filter_value (se fornecido) e exibir os resultados. Ela lida com as duas possibilidades de consulta:

- Com filtro: Filtra os registros de dut_register e, com base nos dut_id encontrados, realiza a consulta na tabela yield_platform.

- Sem filtro: Retorna todos os dados da tabela yield_platform.


#### Resumo do Processo de Registro e Consulta

- Conexão com o banco é estabelecida usando o SQLAlchemy.
- Reflexão das tabelas é feita para obter a estrutura das tabelas existentes no banco.
- Consulta e filtragem dos dados é realizada através de SQLAlchemy, permitindo buscar valores distintos para filtros e realizar seleções baseadas em critérios definidos.
- Execução de consultas SQL é feita por meio de select() e where(), com os resultados sendo obtidos e processados com o método fetchall().
- Exibição dos resultados é feita para o usuário, mostrando os dados filtrados ou todos os dados, conforme a escolha.
- Esse código utiliza a flexibilidade do SQLAlchemy para realizar consultas dinâmicas e interagir com o banco de dados de forma eficiente.

### 3.4 Criar a interface do usuário:

#### Interface com o Usuário:

O código fornece uma interface simples para o usuário escolher o tipo de filtro desejado, exibir os resultados da consulta e permitir a interação. O filtro por batch é uma das opções oferecidas.