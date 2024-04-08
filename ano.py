ano = float(input('insira o ano que voce quer '))
if  ano % 4 == 0 and (ano % 100 != 0 or ano % 400 ==0):
    print(f"o ano {ano} eh bissexto.")
else:
    print(f"o ano {ano} nao eh bissexto.")