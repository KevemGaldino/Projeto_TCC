import luhn
import pyodbc
import difflib
import time
import sys
from twilio.rest import Client
from random import randint

# Validando número de cartão de crédito
def validar_cartao(num_cartao):
    if luhn.verify(num_cartao):
        print("O número do cartão é válido.")
    else:
        print("O número do cartão é inválido.")
        return


# TABELA DO BANCO DE DADOS = DadosCartoes
# Validando dados já existentes
def valida_dados(cod_cartao):
    # Realiza consulta para verificar se os dados já existem ou não
    comando_consulta = f"""SELECT cvc_cartao, nome_cartao FROM DadosCartoes WHERE cvc_cartao = '{cod_cartao}'"""
    cursor.execute(comando_consulta)
    result = cursor.fetchone()
    if result:
        print('Dados do cartão já existe em nosso sistema!')
    # Caso não exista, passa os dados do cliente para o BD
    else:
        comando_insere = f"""INSERT INTO DadosCartoes VALUES ({nome_cartao}, '{data_cartao}', '{cod_cartao}', '{numero_cartao}')""" 
        cursor.execute(comando_insere)
        cursor.commit()
        print('Dados cadastrados com sucesso!')


# TABELA DO BANCO DE DADOS = Cadastro
# Função para comparação de email e nome do cartão
# Essa tabela serve apenas para simular o email logado na conta do ecommerce
def valida_email(nome_cartao):
    consulta_email = f"""SELECT usuario FROM Cadastro WHERE id = '1' """
    cursor.execute(consulta_email)
    dado = cursor.fetchone()
    if dado:
        dado = dado[0]
        print(f'O e-mail de cadastro é {dado}')
        print(f'O nome do cartão é {nome_cartao}')
        dado = dado.lower()
        nome_cartao = nome_cartao.lower()
        similaridade = difflib.SequenceMatcher(None, nome_cartao, dado.split('@')[0]).ratio()
    return similaridade



# TABELA DO BANCO DE DADOS = Contas
# Fazendo uma busca de CPF na tabela de contas cadastradas
def busca_cpf(cpf_titular):
    consulta_cpf = f"""SELECT CPF FROM Contas WHERE CPF = '{cpf_titular}' """
    cursor.execute(consulta_cpf)
    resultado_cpf = cursor.fetchone()
    if resultado_cpf:
        consulta_telefone = f"""SELECT Telefone FROM Contas WHERE CPF = '{cpf_titular}' """
        cursor.execute(consulta_telefone)
        resultado_telefone = cursor.fetchone()
        resultado_cpf = resultado_cpf[0]
        resultado_telefone = resultado_telefone[0]
        print(f'O CPF {cpf_titular} está associado a outra conta, para aprovação de sua compra, por favor, confirme o código enviado por SMS.')
        return resultado_telefone
    else:
        print('Esse CPF não está associado a nenhuma conta em nosso site')
        return None
    


def gera_codigo():
    digitos = str(randint(100000, 999999))
    return digitos


# Função para envio do código por SMS
def enviar_sms(numero_destino, mensagem):
    # Credenciais da conta Twilio
    account_sid = 'ACb74d0d6a13873530ab432f920985e37c'
    auth_token = 'd28bb1144aafcb98047cdc7793dd4537'
    numero_twilio = '(256) 286-5029'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=mensagem,
        from_=numero_twilio,
        to=numero_destino,
    )
    message = message.sid

    print(f"Código de verificação enviado com sucesso!")



# INICIO DO PROGRAMA

#--------------------------------------------------------#
# Criando conexão com o Banco de Dados
dados_conexao = str(
    "Driver={SQL Server};"
    "Server=NOTEKEVEM\SQLEXPRESS;"
    "Database=Ecommerce;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida!')

cursor = conexao.cursor()
#--------------------------------------------------------#

# MENSAGEM DE INICIO DO PROGRAMA
print('Olá, agora iremos verificar seus dados para aprovação da sua compra. Por favor, forneça os dados abaixo: ')
time.sleep(1)

# RECEBENDO DADOS DO CLIENTE E VERIFICAÇÃO DOS DADOS
nome_cartao = input('Digite o nome do proprietário do cartão: ')
data_cartao = input('Digite a data de vencimento do cartão: ')
cvc_cartao = int(input('Digite o código de seguraça (CVC ou CVV) do cartão: '))
numero_cartao = input('Digite o número do cartão de crédito: ')
cpf_titular = input('Digite o CPF do titular do cartão: ')

# validar_cartao(numero_cartao)
valida_dados(cvc_cartao)


# REALIZANDO A COMPARAÇÃO DO NOME DO CARTÃO COM O E-MAIL DE CADASTRO DA CONTA
similaridade_nome_email = valida_email(nome_cartao)
limiar_similaridade = 0.5  # Defina um limiar de similaridade adequado
similaridade_percentual = similaridade_nome_email * 100

if similaridade_nome_email >= limiar_similaridade:
    print('Em análise, por favor aguarde...')
    time.sleep(5)
    print(f"A similariedade é {similaridade_percentual:.1f}%. O nome do cartão é similar ao nome no email pessoal.")
    print('Sua compra será analisada, em breve enviaremos um retorno!')
else:
    print('Em análise, por favor aguarde...')
    time.sleep(5)
    print(f"A similariedade é {similaridade_percentual:.1f}%. O nome do cartão não é similar ao nome no email pessoal.")
    print('Portanto, estamos analisando o CPF digitado, por favor aguarde...')
    time.sleep(5)
    # ENVIO DE CÓDIGO DE VERIFICAÇÃO POR SMS
    codigo_aleatorio = gera_codigo()
    numero_destino = busca_cpf(cpf_titular)
    enviar_sms(numero_destino, mensagem)
    mensagem = f'Olá, seu código de verificação é {codigo_aleatorio}'

   
    cont = 0
    while True:
        cont += 1
        verifica_codigo = str(input('Digite seu código recebido por SMS: '))
        if verifica_codigo == codigo_aleatorio:
            print('Compra aprovada!')
            break
        else:
            print('Código incorreto, tente novamente!')
            time.sleep(2)
            criar_novo_codigo = str(input('Deseja enviar um novo código? [SIM/NAO]')).upper()
            if criar_novo_codigo == 'SIM':
                novo_codigo = gera_codigo()
                mensagem = f'Olá, seu código de verificação é {novo_codigo}'
                enviar_sms(numero_destino, mensagem)
                # print(codigo_aleatorio)
                verifica_codigo = str(input('Digite seu código recebido por SMS: '))
                if verifica_codigo == novo_codigo:
                    print('Compra aprovada!')
                    break
                else:
                    print('Codigo incorreto, você tem mais 3 tentativas!')
                    for i in range(0,3):
                        i += 1
                        verifica_codigo = str(input('Digite seu código recebido por SMS: '))
                        if i == 1:
                            print('Você tem apenas mais 2 tentativas!')
                        if i == 2:
                            print('Você tem apenas mais 1 tentativa!')
                        if i == 3:
                            print('Número de tentativas encerrado\nPor motivos de segurança, estaremos encerrando o sistema!')
                            print('ENCERRANDO...')
                            time.sleep(2)
                            sys.exit()
            elif criar_novo_codigo == 'NAO':
                print('Não enviamos outro código, digite o correto!')
                if cont >= 7:
                    print('Muitas tentativas incorretas, forneça os dados corretos!')
                    print('ENCERRANDO O SISTEMA...')
                    time.sleep(2)
                    sys.exit()
                else:
                    continue
            else:
                print('Opção inválida!')




