print("\n\n")
palavras = [
    {"en": "monday", "pt": "segunda-feira"},
    {"en": "tuesday", "pt": "terça-feira"},
    {"en": "wednesday", "pt": "quarta-feira"},
    {"en": "thursday", "pt": "quinta-feira"},
    {"en": "friday", "pt": "sexta-feira"},
    {"en": "hot", "pt": "quente", "fr": "chand", "es": "caliente"}
]
# perguntando ao usuário de qual idioma se deseja traduzir
idioma = input("De qual idioma se deseja traduzir? ")
# perguntando ao usuário qual palavra se deseja traduzir
palavra = input("Qual palavra se deseja traduzir? ")

print(idioma, palavra)
for traducao in palavras:
    if palavra == traducao.get(idioma):
        for ling, trad in traducao.items():
            if ling != idioma:
                print(f"{palavra} em {ling} é {trad}")
        break


print("\n\n")
frutas = ["Banana", "Maça", "Goiaba"]
for i, fruta in enumerate(frutas):
    print(i, fruta)