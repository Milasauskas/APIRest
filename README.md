# APIRest

API Client criado para listar todas as raças.

Para realizar a criação da API necessitamos:
-criação do ambiente
- Instalação do python
- Intalação do Pycharm

Após as realizar a instalações dos software acima, devemos iniciar a configuração do ambiente, para iniciar o desenvolvimento.

Clicar em File - New Project
Informar o Location: C:\Users\Danielle Pereira\PycharmProjects\APIRest.
Selecionar a opção: New environment using: Virtualenv
Clicar em Create

Após Criar o ambiente, Clicar em File -> Settings
Clicar no project APIRest -> Phyton Interpreter
Clicar duas vezes em cima de pip
Pesquisar o nome Flask
Selecionar e clicar em Install Package

Assim que finalizar a instação, ficara uma tarja verde mostrando que foi concluido.
Clicar em Fechar.

Finalizando a instalação do Flask, faremos o mesmo processo para o SQLAlchemy

Clicar em File -> Settings
Clicar no project APIRest -> Phyton Interpreter
Clicar duas vezes em cima de pip
Pesquisar o nome SQLAlchemy
Selecionar e clicar em Install Packag

Realizaremos o mesmo passao a passo para o Restless

Clicar em File -> Settings
Clicar no project APIRest -> Phyton Interpreter
Clicar duas vezes em cima de pip
Pesquisar o nome Flask-Restless
Selecionar e clicar em Install Packag

Fianlizando essa instação podemos iniciar a configuração do ambiente.

Iremos criar a seguinte estrutura:

App
database
Models
Routes

Os diretórios sempre serão criados app/models
                                   app/database
                                   app/models
                                   app/routes

Criando os diretórios cima, vamos fazer com ele eles virem módulos, para eles virarem modulos,
vamos criar um arquivo __init__.py em cada diretório.
Também vamos criar uma arquivo com o nome run.py, para executarmos nossa API.

Após a criação de toda a estrutura que fizemos iniciamos nosso desenvolvimento, que seria:

API capaz de listar todas as raças
API capaz de listar as informações de uma raça
API capaz de a partir de um temperamento listar as raças
API capaz de a partir de uma origem listar as raças 

Após a criação das APIs, temos que também ter os Json no postamn, para conseguirmos realizar as consultas das API,
inserir dados na APIS, excluir  e conseguir realizar as manupulações dos dados.




