"""
O presente código tem por objetivo selecionar aleatoriamente
outros arquivos .py e executá-los, tratam-se de jogos madlibs
que serão selecionados de forma aleatória para o usuário jogar
dentro do terminal

"""
import os
import random
import subprocess

def selecionar_jogo_madlib(diretorio):
    # Obter a lista de todos os arquivos Python no diretório
    arquivos_python = [f for f in os.listdir(diretorio) if f.endswith('.py')]
    
    # Verificar se há arquivos Python no diretório
    if not arquivos_python:
        print("Não há arquivos Python no diretório especificado.")
        return None
    
    # Selecionar aleatoriamente um arquivo Python
    arquivo_selecionado = random.choice(arquivos_python)
    caminho_arquivo_selecionado = os.path.join(diretorio, arquivo_selecionado)
    
    return caminho_arquivo_selecionado

def executar_jogo_madlib(caminho_arquivo):
    print(f"\nExecutando o jogo MadLib: {os.path.basename(caminho_arquivo)}")
    print("-" * 50)
    
    # Executar o arquivo Python selecionado
    resultado = subprocess.run(['python', caminho_arquivo], capture_output=True, text=True)
    
    # Imprimir a saída do arquivo executado
    print(resultado.stdout)
    print(resultado.stderr)
    print("-" * 50)

def main():
    diretorio = r'C:\Users\EMIDIO\python-base\sample_madlibs'  
    
    print("Bem-vindo ao jogo MadLib aleatório!\n")
    
    # Selecionar e executar um jogo MadLib
    jogo_selecionado = selecionar_jogo_madlib(diretorio)
    if jogo_selecionado:
        executar_jogo_madlib(jogo_selecionado)
    else:
        print("Nenhum jogo MadLib encontrado.")

if __name__ == "__main__":
    main()


