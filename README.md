# Projeto_TCC - Validação de compras onlines com cartões de crédito
Projeto em Python para fraudes de cartões de crédito

Esse projeto tem como objetivo fazer a validação do nome do cartão de crédito pessoal com o e-mail cadastrado na conta da plataforma que o usuário está logado.

# EXPLICANDO AS IMPORTAÇÕES

import luhn:

import pyodbc:

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





