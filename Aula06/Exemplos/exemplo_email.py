import requests
import json
import os

print("\n\n")
# print("Dir", os.getcwd()) -> current working directory

BASE_DIR = "Aula06/Exemplos/" # mudar esse valor para caminho absoluto ou caminho relativo
TEMPLATE_PATH = BASE_DIR + "arquivos/email_base.html"
TRANSLATE_PATH = BASE_DIR + "arquivos/translate.json"

def open_traducoes() -> dict:
    """
    Abre o arquivo json de traduções e o converte para um objeto dict
    :raises FileNotFoundException:
    """
    with open(TRANSLATE_PATH, "r") as json_data:
        content = json_data.read()
        return json.loads(content)

def open_template() -> str:
    """
    Abre o arquivo html base, lê o seu conteúdo e retorna em forma de string.
    :return: string que possui o conteúdo lido do arquivo base
    :raises FileNotFoundException:
    """
    with open(TEMPLATE_PATH, "r") as base:
        return base.read()

def render_delivery(email_template: str, user: dict, product: dict) -> str:
    name = user.get("name")
    item_name = product.get("name")
    email_template = email_template.replace("%NOME%", name)
    email_template = email_template.replace("%PRODUTO%", item_name)
    return email_template

def render_email(email_template: str, lang="en", _type="delivery_update") -> str:
    """
    Renderiza o texto passado, i.e. substitui as tags marcadas por suas respectivas traduções
    :param email_template: string que possui o conteúdo a ser renderizado
    :param lang: string contendo a linguagem a qual será utilizada para renderizar (pt | en)
    :return: string que possui o conteúdo renderizado na língua informada
    """
    trads = open_traducoes() # OK
    for key, trad in trads.items():
        key = key.upper()
        trad = trad.get(lang)
        email_template = email_template.replace(f"%{key}%", trad)
    
    # atualizar chaves dinâmicas (pelo tipo de operação)
    key = "email_body_" + _type
    trad = trads.get(key).get(lang)
    email_template = email_template.replace(f"%EMAIL_BODY%", trad)

    return email_template
    

def save_render(render: str, path: str):
    """
    Salva o arquivo renderizado no diretório passado
    :param render: string que possui o conteúdo renderizado
    :param path: string contendo o caminho relativo ou absoluto para salvar o arquivo
    """
    with open(path, "w") as arqv:
        arqv.write(render)
    

if __name__ == "__main__":
    user = {"id": 123, "name": "Caroline"}
    item = {"id": 123, "name": "Notebook i9", "price": 1999.99}

    email_template = open_template() # OK
    print(email_template, "\n")
    render = render_email(email_template, "pt")
    render = render_delivery(render, user, item)
    print(render)
    save_render(render, "Aula06/Exemplos/arquivos/email_render.html")

