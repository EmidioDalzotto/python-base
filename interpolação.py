email_tmpl = """
        Olá, %(nome)s 
        tem interesse em comprar %(produto)s?
   ...: 
   ...: Este produto é ótimo para resolver %(texto)s
   ...: %(texto)s
   ...: 
   ...: Clique agora em %(link)s
   ...:
   ...: Preço promocional %(preco).2f
   ...:
   ...: """

clientes = ["João", "William", "Gustavo"]
for cliente in clientes:
 print(email_tmpl % { "nome": cliente, "produto": "caneta", 
        "texto": "Escreve de forma satisfatória e agradá vel", 
        "link": "https//:canetaslegais.com", 
        "quantidade": 1, 
        "preco": 50.0
   }
)
