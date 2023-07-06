import pickle

def abrirArquivo(caminhoArquivo):
    with open(caminhoArquivo, "rb") as file:
        return pickle.load(file)

def escolha():
    print("Digite o número correspondente a quantidade de alunos que serão informados como entrada:")
    entradas = ["1 - 10 alunos.","2 - 100 alunos.","3 - 1000 alunos.","4 - 10000 alunos.","5 - 100000 alunos.","6 - 1000000 alunos."]
    for i in entradas:
        print(i)

    opcao = int(input("Opção: "))

    while opcao<1 or opcao>6:
        opcao = int(input("Opção inválida! Digite um número dentre as opções descritas acima: "))

    if opcao == 1:
        return "entradas/entrada10.bin"
    if opcao == 2:
        return "entradas/entrada100.bin"
    if opcao == 3:
        return "entradas/entrada1000.bin"
    if opcao == 4:
        return "entradas/entrada10000.bin"
    if opcao == 5:
        return "entradas/entrada100000.bin"
    if opcao==6:
        return "entradas/entrada1000000.bin"

def antecessor(d, x, y):
#verificando ano
    if d[x][1][0] > d[y][1][0]: return True
    if d[x][1][0] < d[y][1][0]: return False

#verificando semestre
    if d[x][1][1] > d[y][1][1]: return True
    if d[x][1][1] < d[y][1][1]: return False

#verificando nota final
    if d[x][3] == 0: nfx = sum(d[x][2])+2
    else: nfx = sum(d[x][2])

    if d[y][3] == 0: nfy = sum(d[y][2])+2
    else: nfy = sum(d[y][2])

    if nfx > 100: nfx = 100
    if nfy > 100: nfy = 100

    if nfx > nfy: return True
    if nfx < nfy: return False

#ordem alfabetica
    if d[x][0] < d[y][0]: return True
    if d[x][0] > d[y][0]: return False

#por matricula
    if x < y: return True
    if x > y: return False

    return True

def trocaElemento(l, x, y):
    aux = l[x]
    l[x] = l[y]
    l[y] = aux

def mergeSort(l, d):
    if len(l) > 1:
        meio = len(l)//2
        lesq = l[:meio]
        ldir = l[meio:]
        mergeSort(lesq, d)
        mergeSort(ldir, d)

        merge(l, d, lesq, ldir)

def merge(l, d,  lesq, ldir):
    i = 0
    j = 0
    k = 0

    while i < len(lesq) and j < len(ldir):
        if antecessor(d, lesq[i], ldir[j]):
        #if lesq[i] < ldir[j]:
            l[k] = lesq[i]
            i += 1
        else:
            l[k] = ldir[j]
            j += 1
        k += 1

    while i < len(lesq):
        l[k] = lesq[i]
        i += 1
        k += 1

    while j < len(ldir):
        l[k] = ldir[j]
        j += 1
        k += 1

def escreva(matriculas, dicionario):
    saida = open("saida.txt", "w")
    for matricula in matriculas:
        saida.write("{}/{} {} {} - ".format(dicionario[matricula][1][0], dicionario[matricula][1][1], matricula,
                                            dicionario[matricula][0]))

        if dicionario[matricula][3] == 0:
            notaTotal = sum(dicionario[matricula][2]) + 2
        else:
            notaTotal = sum(dicionario[matricula][2])

        if notaTotal > 100:
            notaFinal = 100
        else:
            notaFinal = notaTotal

        saida.write("{} ".format(notaFinal))

        n1 = dicionario[matricula][2][0]
        n2 = dicionario[matricula][2][1]
        n3 = dicionario[matricula][2][2]
        bonus = dicionario[matricula][2][3]

        if bonus == 0 and dicionario[matricula][3] == 0:
            saida.write("({}+{}+{} +2P = {})\n".format(n1, n2, n3, notaTotal))
        if bonus != 0 and dicionario[matricula][3] == 0:
            saida.write("({}+{}+{} +{}E +2P = {})\n".format(n1, n2, n3, bonus, notaTotal))
        if bonus == 0 and dicionario[matricula][3] != 0:
            saida.write("({}+{}+{} = {})\n".format(n1, n2, n3, notaTotal))
        if bonus != 0 and dicionario[matricula][3] != 0:
            saida.write("({}+{}+{} +{}E = {})\n".format(n1, n2, n3, bonus, notaTotal))

    saida.close()