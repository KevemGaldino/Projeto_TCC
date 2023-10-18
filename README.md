# Projeto_TCC - Validação de compras onlines com cartões de crédito
Projeto em Python para fraudes de cartões de crédito

Esse projeto tem como objetivo fazer a validação do nome do cartão de crédito pessoal com o e-mail cadastrado na conta da plataforma que o usuário está logado.

# EXPLICANDO AS IMPORTAÇÕES

import luhn:
O algoritmo de Luhn é bem utilizado para validar números de cartões de crédito. Ele funciona fazendo uma soma ponderada dos dígitos do número, seguido por uma verificação se a soma dos valores é um múltiplo de 10.

Os passos básicos para o algoritimo de Luhn são:

É necessário começar da direita para a esquerda, ou seja, se o número do cartão for 123456789, é preciso invertê-lo, 987654321;

Após isso, cada segundo dígito é duplicado, caso a duplicação for maior que 9, deve-se subtrair 9 desse resultado;

Em seguida, deve ser feito a soma de todos os dígitos, se o resultado da soma for um múltiplo de 10, então o número do cartão é válido.

import pyodbc:
O módulo pyodbc é uma interface do Python para acessar um banco de dados utilizando o ODBC (Open Database Connectivity). O ODBC é uma API (Aplication Programing Interface) que permite várias linguagens de programação criar conexões com diferentes banco de dados, basta somente especificar o driver correto para qual SGBD (Sistema Gerenciador de Banco de Dados) vai ser aplicado.
Para utilizar o pyodbc, é necessário seguir alguns passos, dentre eles são: 
- Instalar o módulo com o comando "pip install pyodbc";
- Criar a conexão com o comando "pyodbc.connect()", é necessário fornecer uma string informando os dados de acesso como driver, servidor e nome do banco de daods.
- Criar um cursor com o comando "connection.cursor()" para executar as consultas SQL e obter dados.
- Criar uma recuperação de resultados com o comando "cursor.fetchone()" para retornar valoress específicos.
Em suma, o pyodbc oferece uma maneira flexível e eficiente para trabalhar com diferentes tipos de bancos de dados por meio da linguagem Python.

import difflib:

import time:

import sys:

from twilio.rest import Client:

from random import randint:

# EXPLICANDO AS FUNÇÔES
No código, temos 6 funções:

Primeira função: verificar se o número do cartão é válido, para isso utilizei a biblioteca luhn.

Segunda função: a função valida os dados inseridos, verificar se os dados já existem ou não em uma tabela do banco de dados, caso não exista e passe pelos requisitos de segurança do código, os dados são inseridos.

Terceira função: nessa função, suponhamos que já sabemos o email de cadastro, ele puxa um email específico e realiza a comparação com o nome do cartão digitado. A função indica uma porcentagem de similaridade entre o nome do cartão e nome do email.

Quarta função: de acordo com o CPF digitado pelo usuário, a função faz uma busca desse CPF na tabela de contas cadastradas e retorna um número de telefone associado ao CPF.

Quinta função: nessa função, é gerado um conjunto de números aleatórios de 6 dígitos, iniciando de 100000 até 999999.

Sexta função: a função cria uma mensagem de acordo com os dados utilizados da Twilio. É necessário criar uma conta no site da Twilio, assim é gerado um ID da conta, um token de autenticação e um número virtual, para envio de mensagens. Nesse caso, a função só enviará mensagens para dois telefones cadastrados no site da Twilio, pois é o plano gratuito, caso queira enviar mensagens para qualquer número, é necessário adquirir um plano pago.

# INÍCIO DO PROGRAMA
No início do programa primeiramente é feito uma conexão com o banco de dados SQL Server e criado um cursor, para enviar os comandos SQL via python;
É definido as variáveis solicitando os dados do cartão do cliente;
Foi criado uma variável para extrair a similaridade do nome do cartão com o nome do e-mail;
Sendo assim, é feito um IF/ELSE, caso a similaridade seja maior que o limite definido, a compra será aprovada;
Caso a similaridade seja inferior ao limite estipulado, é feito uma busca do CPF digitado, verificando se já existe uma conta associada a esse CPF no site do ecommerce. Caso exista, é gerado um código aleatório e enviado por SMS no número de telefone associado ao CPF. Após isso, o usuário é redirecionado a um loop, onde é solicitado o código enviado por SMS e só é liberado com o código correto. 

# LEMBRETE
CRIAR UMA VALIDAÇÃO DE CPF





