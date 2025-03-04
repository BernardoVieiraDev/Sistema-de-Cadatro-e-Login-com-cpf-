import sys
import os
from tkinter import PhotoImage

def carregar_imagem(nome_arquivo):
    """
    Função para carregar a imagem corretamente tanto no modo desenvolvimento quanto no executável.
    :param nome_arquivo: Nome do arquivo da imagem (como 'eye.png')
    :return: Objeto PhotoImage carregado ou None se houver erro.
    """
    # Verifica se o script está sendo executado a partir de um executável gerado pelo PyInstaller
    if getattr(sys, 'frozen', False):
        # Diretório temporário onde o PyInstaller coloca os arquivos
        base_path = sys._MEIPASS #type: ignore
    else:
        # Diretório atual do script durante o desenvolvimento
        base_path = os.path.abspath('.')
    
    # Caminho completo para o arquivo de imagem
    caminho_imagem = os.path.join(base_path, nome_arquivo)

    try:
        # Carregar e retornar a imagem
        return PhotoImage(file=caminho_imagem)
    except Exception as e:
        print(f"Erro ao carregar imagem '{nome_arquivo}': {e}")
        return None
