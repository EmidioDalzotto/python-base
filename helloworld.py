"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente 
o programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
export LANG=pt_BR

ou informe através do CLI argument '--lang'
assim como '--count=número'
ou o usuário terá de digitar
"""
__version__ = "0.1.3"
__author___ = "tal de tal"
__license__ = "unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": None,
}
for arg in sys.argv[1:]:
    # TODO: TRATAR ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print("Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar Repetição
    if "LANG" in os.environ: 
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")


current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print (
    msg[current_language] * int(arguments["count"])
  )

