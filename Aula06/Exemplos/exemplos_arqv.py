print("\n\n")

try:
    #arq_path_abs = "/home/yagorezende/VSCodeProjects/Aulas/Aula06/Exemplos/arquivos/poema.txt"
    arq_path = "Aula06/Exemplos/arquivos/poema.txt" # caminho relativo
    arq = open(arq_path, "r") # r = read
except FileNotFoundError as fnf:
    print("Arquivo não encontrado", fnf)
else:
    # cuidados com isso: não façam leituras inteiras em arqvs grandes
    #linhas = arq.readlines()
    #for linha in linhas:
    #    print(linha, end="")
    linha = arq.readline()
    while linha:
        print(linha, end="")
        linha = arq.readline()
finally:
    try:
        arq.close()
    except:
        pass
print()


try:
    #arq_path_abs = "/home/yagorezende/VSCodeProjects/Aulas/Aula06/Exemplos/arquivos/poema.txt"
    arq_path = "Aula06/Exemplos/arquivos/exemplo_teste.txt" # caminho relativo
    arq = open(arq_path, "w") # r = read
except FileNotFoundError as fnf:
    print("Arquivo não encontrado", fnf)
else:
    arq.write("Tubarão\n")
    arq.write("O Poderoso Chefão\n")
finally:
    try:
        arq.close()
    except:
        pass


print("Usando comando with")
arq_path = "/Aula06/Exemplos/arquivos/poema.txt" # caminho relativo
try:
    with open(arq_path, "r") as arqv:
        for linha in arqv.readlines():
            print(linha, end="")
except FileNotFoundError as fnf:
    print("Arquivo não encontrado", fnf)
print()
