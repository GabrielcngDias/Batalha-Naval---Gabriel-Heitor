from funcoes import define_posicoes, preenche_frota, posicao_valida

frota = {}

navios = [
    ["porta-aviões", 4, 1],
    ["navio-tanque", 3, 2],
    ["contratorpedeiro", 2, 3],
    ["submarino", 1, 4]
]

for navio in navios:
    nome = navio[0]
    tamanho = navio[1]
    quantidade = navio[2]

    i = 0
    while i < quantidade:
        print("Insira as informações referentes ao navio " + nome + " que possui tamanho " + str(tamanho))
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if nome == "submarino":
            orientacao = "vertical"
        else:
            escolha = int(input("[1] Vertical [2] Horizontal >"))
            if escolha == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            i = i + 1
        else:
            print("Esta posição não está válida!")

print(frota)