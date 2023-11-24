data = input("Digite um mês no padrão dd/mm/aa:" )

#coloca os valores recebidos em uma array separando eles pelos caracteres "/"
dia, mes, ano = data.split("/")

#transforma os valores recebidos em inteiros
dia, mes, ano = int(dia), int(mes), int(ano)

#variavel para imprimir quanda a data for inválida
error = "Data inválida!!"

#função para verificar a data recebida
def verificaData(dia, mes, ano):
    global error
    #método para verificar o ano e o mes
    if ano < 1 or ano > 2023:
        return error
    elif mes < 1 or mes > 12:
        return error

#método para validar o dia em meses que possuem 31 dias
    elif mes in[1, 3, 5, 7, 8, 10, 12]:
        if dia < 1 or dia > 31:
            return error

#método para validar o dia em meses que possuem 30 dias
    elif mes in [4, 6, 9, 11]:
        if dia < 1 or dia > 30:
            return error
        
#método para validar o mes de fevereiro
    elif mes in [2]:
        if dia < 1 or dia > 28:
            return error
        
#método para validar o mes de fevereiro caso seja um ano bissexto
    if ano // 4 == 0:
        for mes in [2]:
            if dia < 1 or dia > 29:
                return error
print(error)
verificaData(dia, mes, ano)