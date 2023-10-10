# Projeto_TCC
Projeto em Python para fraudes de cartões de crédito

Esse projeto tem como objetivo fazer a validação do nome do cartão de crédito pessoal com o e-mail cadastrado na conta da plataforma que o usuário está logado.

No código, temos 6 funções:

Primeira função: verificar se o número do cartão é válido, para isso utilizei a biblioteca luhn.


Segunda função: a função valida dados, verificar se os dados do cartão inseridos já existem ou não em uma tabela do banco de dados, caso não exista, os dados são inseridos. Porém, nessa tabela, não estamos adicionando o CPF

No início do programa primeiramente fazemos uma conexão com o banco de dados SQL Server e criamos um cursor, para enviar os comandos SQL via python;
Após isso, definimos as variáveis solicitando os dados do cartão do cliente e assim utilizar as funções criadas;

Em breve, estarei colocando como vou fazer a comparação do email e nome do cartão.

Adicionado recentemente o código completo.

A intenção desse código é:




