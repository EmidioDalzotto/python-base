numeros = list(range(1 ,11))

# para cada numero em numeros:
for n1 in numeros:
    print ("{:-^18}".format("Tabuada do 2"))
    print ()
    for n2 in numeros:
        resutado = n1 * n2
        print (f"{n1} x {n2} = {resultado}")
    
    print (tamplate.format(bloco=bloco))
    
