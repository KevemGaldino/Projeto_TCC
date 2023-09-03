# Projeto_TCC
Projeto em Python para fraudes de cartões de crédito

Esse projeto tem como objetivo fazer a validação do nome de cartão de crédito pessoal com o e-mail cadastrado na conta da plataforma que o usuário está logado.

No código inicial, temos duas funções, uma pra verificar se o número do cartão é válido, para isso utilizei a biblioteca luhn.
A outra função é para verificar se os dados inseridos já existem ou não no banco de dados.

No início do programa primeiramente fazemos uma conexão com o banco de dados SQL Server e criamos um cursor, para enviar os comandos SQL via python;
Após isso, definimos as variáveis solicitando os dados do cartão do cliente e assim utilizar as funções criadas;

Em breve, estarei colocando como vou fazer a comparação do email e nome do cartão.

