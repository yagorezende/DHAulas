dias = [
    {"en": "monday", "pt": "segunda-feira"},
    {"en": "tuesday", "pt": "terça-feira"},
    {"en": "wednesday", "pt": "quarta-feira"},
    {"en": "thursday", "pt": "quinta-feira"},
    {"en": "friday", "pt": "sexta-feira"}
]
# perguntando ao usuário de qual idioma se deseja traduzir
idioma = input("Qual idioma se deseja traduzir? ")
# perguntando ao usuário qual dia se deseja traduzir
dia = input("Qual dia se deseja traduzir? ")

print(idioma, dia)

if dias[0][idioma] == dia:
    # Pegando a chave do idioma que se deseja traduzir
    p_traduzir = list(dias[0].keys())
    p_traduzir.remove(idioma)
    idioma_trad = p_traduzir[0]
    # imprimindo o dia traduzido
    print(f"{dia} em {idioma_trad} é {dias[0][idioma_trad]}")
elif dias[1][idioma] == dia:
    # Pegando a chave do idioma que se deseja traduzir
    p_traduzir = list(dias[1].keys())
    p_traduzir.remove(idioma)
    idioma_trad = p_traduzir[0]
    # imprimindo o dia traduzido
    print(f"{dia} em {idioma_trad} é {dias[1][idioma_trad]}")
elif dias[2][idioma] == dia:
    # Pegando a chave do idioma que se deseja traduzir
    p_traduzir = list(dias[2].keys())
    p_traduzir.remove(idioma)
    idioma_trad = p_traduzir[0]
    # imprimindo o dia traduzido
    print(f"{dia} em {idioma_trad} é {dias[2][idioma_trad]}")
elif dias[3][idioma] == dia:
    # Pegando a chave do idioma que se deseja traduzir
    p_traduzir = list(dias[3].keys())
    p_traduzir.remove(idioma)
    idioma_trad = p_traduzir[0]
    # imprimindo o dia traduzido
    print(f"{dia} em {idioma_trad} é {dias[3][idioma_trad]}")
elif dias[4][idioma] == dia:
    # Pegando a chave do idioma que se deseja traduzir
    p_traduzir = list(dias[4].keys())
    p_traduzir.remove(idioma)
    idioma_trad = p_traduzir[0]
    # imprimindo o dia traduzido
    print(f"{dia} em {idioma_trad} é {dias[4][idioma_trad]}")
else:
    print("Essa palavra não está contida no dicionário")
