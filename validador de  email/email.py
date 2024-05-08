def verificar_dominio(email):
    dominios_populares = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']

    partes = email.split("@")
    if len(partes) != 2:
        return False

    dominio = partes[1].lower()  # Convertendo o domínio para minúsculas para garantir correspondência correta

    if dominio in dominios_populares:
        return 'popular'
    else:
        return 'próprio'

email = input("Digite o seu endereço de email: ")
tipo_dominio = verificar_dominio(email)
print('O tipo de domínio do email é:', tipo_dominio)
