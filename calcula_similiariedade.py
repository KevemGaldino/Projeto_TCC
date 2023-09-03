import difflib

def calcula_similaridade(string1, string2):
    return difflib.SequenceMatcher(None, string1, string2).ratio()

nome_cartao = "Kevem C Galdino"
email_pessoal = "kevemcandido1827@gmail.com"

t1 = nome_cartao
t2 = email_pessoal

# Calcula a similaridade entre o nome do cartão e o email pessoal
similaridade = calcula_similaridade(t1.lower(), email_pessoal.split('@')[0].lower())

limiar_similaridade = 0.5  # Defina um limiar de similaridade adequado

if similaridade >= limiar_similaridade:
    print(f"A similariedade é {similaridade:.2f}. O nome do cartão é similar ao nome no email pessoal.")
else:
    print(f"A similariedade é {similaridade:.2f}. O nome do cartão não é similar ao nome no email pessoal.")

print(t1)
print(t2)
