def escreva (msg):
    linha = len(msg) + 4
    print("-" * int(linha))
    print(f'  {msg}')
    print("-" * int(linha))

escreva("teste")
escreva("Olá, Mundo!")
escreva("Emidio")
