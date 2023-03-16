string = input('insira um texto: ')
caracteres_lista = list(string)

inicio = 0
fim = len(caracteres_lista) - 1

while fim > inicio:
    temp = caracteres_lista[inicio]
    caracteres_lista[inicio] = caracteres_lista[fim]
    caracteres_lista[fim] = temp 

    inicio += 1
    fim -= 1
    
string_invertida = "".join(caracteres_lista)

print(f"string original: {string}")
print(f"string invertida: {string_invertida}")
