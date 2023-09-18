import luhn
import pyodbc
import difflib

# Validando número de cartão de crédito
def validar_cartao(num_cartao):
    if luhn.verify(num_cartao):
        print("O número do cartão é válido.")
    else:
        print("O número do cartão é inválido.")
        return


# Validando dados já existentes
def valida_dados(cod_cartao):
    comando_consulta = f"""SELECT cvc_cartao, nome_cartao FROM Dados_de_cartoes WHERE cvc_cartao = '{cod_cartao}'"""
    cursor.execute(comando_consulta)
    result = cursor.fetchone()
    if result:
        print('Dados já existentes!')
        # sys.exit()
    # Passando dados do cliente para o Banco de Dados
    else:
        comando_insere = f"""INSERT INTO Dados_de_cartoes VALUES ('', '', '{cod_cartao}', '')"""  #'{nome_cartao}', '{data_cartao}', '{numero_cartao}'
        cursor.execute(comando_insere)
        cursor.commit()
        print('Dados cadastrados com sucesso!')

# Fazendo a consulta do e-mail no banco de dados
def valida_email(nome_cartao):
    consulta_email = f"""SELECT usuario FROM Cadastro WHERE id = '2' """
    cursor.execute(consulta_email)
    dado = cursor.fetchone()
    if dado:
        dado = dado[0]
        print(dado)
        print(nome_cartao)
        limiar_similaridade = 0.5  # Defina um limiar de similaridade adequado
        dado = dado.lower()
        nome_cartao = nome_cartao.lower()
        similaridade = difflib.SequenceMatcher(None, nome_cartao, dado.split('@')[0]).ratio() # Faz a comparação do nome do cartão com o nome do email cadastrado e retorna um percentual de similiaridade
        if similaridade >= limiar_similaridade:
            print(f"A similariedade é {similaridade:.2f}. O nome do cartão é similar ao nome no email pessoal.")
        else:
            print(f"A similariedade é {similaridade:.2f}. O nome do cartão não é similar ao nome no email pessoal.")


#INICIO DO PROGRAMA

# Criando conexão com o Banco de Dados
dados_conexao = str(
    "Driver={SQL Server};"
    "Server=NOTEKEVEM\SQLEXPRESS;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida!')

cursor = conexao.cursor()

# Recebendo dados do cliente
print('Olá, agora iremos verificar seus dados para aprovação da sua compra. Por favor, forneça os dados abaixo: ')

nome_cartao = input('Digite o nome do proprietário do cartão: ')
# data_cartao = input('Digite a data de vencimento do cartão: ')
cvc_cartao = int(input('Digite o código de seguraça (CVC ou CVV) do cartão: '))
# numero_cartao = input('Digite o número do cartão de crédito: ')
  
# validar_cartao(numero_cartao)
valida_dados(cvc_cartao)
valida_email(nome_cartao)
