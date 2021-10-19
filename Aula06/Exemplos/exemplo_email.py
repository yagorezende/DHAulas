import requests
import json
import os

print("\n\n")
# print("Dir", os.getcwd()) -> current working directory

BASE_DIR = "" # mudar esse valor para caminho absoluto ou caminho relativo
TEMPLATE_PATH = BASE_DIR + "arquivos/email_base.html"
TRANSLATE_PATH = BASE_DIR + "arquivos/translate.json"

def open_traducoes() -> dict:
    """
    Abre o arquivo json de traduções e o converte para um objeto dict
    :raises FileNotFoundException:
    """

def open_template() -> str:
    """
    Abre o arquivo html base, lê o seu conteúdo e retorna em forma de string.
    :return: string que possui o conteúdo lido do arquivo base
    """

def render_email(email_template: str, lang="en") -> str:
    """
    Renderiza o texto passado, i.e. substitui as tags marcadas por suas respectivas traduções
    :param email_template: string que possui o conteúdo a ser renderizado
    :param lang: string contendo a linguagem a qual será utilizada para renderizar (pt | en)
    :return: string que possui o conteúdo renderizado na língua informada
    """

def save_render(render: str, path: str):
    """
    Salva o arquivo renderizado no diretório passado
    :param render: string que possui o conteúdo renderizado
    :param path: string contendo o caminho relativo ou absoluto para salvar o arquivo
    """
    

if __name__ == "__main__":
    email_template = open_template()
    render = render_email(email_template)
    print(render)
    save_render(render, "Aula06/Exemplos/arquivos/email_render.html")

