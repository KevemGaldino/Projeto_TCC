import luhn
import pyodbc


# Validando número de cartão de crédito
def validar_cartao(num_cartao):
    if luhn.verify(num_cartao):
        print("O número do cartão é válido.")
    else:
        print("O número do cartão é inválido.")
        return


# Validando dados já existentes
def valida_dados(cod_cartao):
    comando_consulta = f"""SELECT cvc_cartao FROM Dados_de_cartoes WHERE cvc_cartao = '{cod_cartao}'"""
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


# def valida_email(nome_cartao):
#     consulta_email = f"""SELECT email FROM Clientes WHERE  """



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

# nome_cartao = input('Digite o nome do proprietário do cartão: ')
# data_cartao = input('Digite a data de vencimento do cartão: ')
cvc_cartao = int(input('Digite o código de seguraça (CVC ou CVV) do cartão: '))
numero_cartao = input('Digite o número do cartão de crédito: ')
  
validar_cartao(numero_cartao)
valida_dados(cvc_cartao)
