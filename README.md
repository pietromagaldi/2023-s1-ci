# Exercício de integração contínua

## Problema
Esse repositório implementa uma API HTTP para validar o texto de uma senha 
de acordo com alguns critérios. Entretanto, o código está incompleto e possui
bugs, o seu trabalho é consertá-lo, completá-lo e rodar o pipeline.<br>

Este repositório foi desenvolvido utilizando o gerenciador de pacotes 
**poetry**, mas você não precisa dele. Basta utilizar os arquivos
de dependências requirements.txt e requirements-dev.txt<br>

### Os critérios para senhas válidas são:
1. Mínimo de 8 caracteres<br>
2. Pelo menos 1 número<br>
3. Pelo menos 1 caractere especial<br>
4. Pelo menos 1 letra maiúscula<br>
5. Pelo menos 1 letra minúscula<br>
6. Caracteres especiais não podem ser / ^ ~<br>

# Tarefas
## 0. Faça o fork do projeto no github;
## 1. Faça o clone do seu fork na sua máquina;
## 2. Verifique que os testes não cobrem a especificação e adicione testes e implementação adequados;
## 3. Rode o seu pipeline com sucesso.

# Instalando o ambiente de desenvolvimento

## Development environment dependencies
| Dependencies      | Tested Version | Minimum Version | Url                                                            |
|-------------------|----------------|-----------------|----------------------------------------------------------------|
| Python            | 3.13           | 3.7.5           | [link](https://www.python.org/downloads/release/python-3130/)  |
| Poetry (optional) | 1.2.0          | 1.0.0           | [link](https://python-poetry.org/)                             |

### clone o seu fork
````shell
$ git clone git@github.com:...XXXX.../2023-s1-ci.git
````

### Instalando as dependências
````shell
$ cd 2023-s1-ci/
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
````

## Rodando a aplicação web
````shell
$ cd 2023-s1-ci
$ uvicorn simple_web_app.main:app --reload
````

## Rodando os testes
````shell
$ cd 2023-s1-ci
$ pytest
````
