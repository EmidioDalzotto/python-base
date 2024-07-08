"""
Madlibs são textos prontos com espaços em branco onde o jogador
vai declarar verbos, adjetivos ou nomes e estas informações serão
utilizadas para preencher o texto previamente estabelecido.

O objetivo deste projeto é produzir diversos madlibs com f"..{}."
após dar input para o usuário declarar verbos e adjetivos, então
randomicamente selecionar dentre os madlibs prontos aquele que será
preenchido

"""

# exemplo:

local1 = input("um lugar?: ")
verb1 = input("verbo: ")
fruta1 = input("uma fruta?: ")

madlib = f"Seu José foi para a {local1}, para {verb1}, enquanto \
isso Maria tinha ido colher {fruta1} no quintal da vizinha" 

print(madlib)