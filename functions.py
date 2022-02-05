
# Biblioteca Import para geração de números aleatórios e Biblioteca Time para exibir os resultados gradativamente
from random import randint
from time import sleep


# Função para iniciar o jogo
def iniciar():
    print("-- INÍCIO DO JOGO --")

    # Recebimento da quantidade de cartelas
    num = int(input("\nNúmero de cartelas: "))
    sleep(0.1)

    # Retornar a quantidade de cartelas
    print(f"{num} cartela(s) criada(s)!")

    return num


# Função para criar as cartelas
def criar_cartela(x):
    cartelas = list()

    # Preencher todas as cartelas com números aleatórios sem repetição
    for i in range(x):
        cartela = list()

        while len(cartela) != 10:
            n = randint(1, 25)

            if n not in cartela:
                cartela.append(n)

        # Adicionando os números aleatórios às cartelas
        cartelas.append(cartela)

        # Adicionando o índice responsável pela pontuação à respectiva cartela
        cartelas[i].append(0)

    return cartelas


# Função para sortear os números nas cartelas
def sorteio(x):
    sleep(0.5)

    print("\n-- Iniciando sorteio --\n")

    sleep(0.5)
    resultado = list()
    ganhadores = list()

    # Preencher todas as cartelas com números aleatórios sem repetição
    while len(resultado) != 25:
        n = randint(1, 25)

        if n not in resultado:
            resultado.append(n)

            print(f"O número sorteado foi: {n}")

            sleep(0.5)

            # Puxando função de pontuação e verificando se há ganhadores
            r = conferir(x, n, resultado, ganhadores)

            """
            Após r se tornar uma matriz com os um valor True/False e uma lista de ganhador(es)/vazia,
            a função irá verificar se este primeiro valor é True ou False, caso seja True, o programa irá encerrar
            exibindo os ganhadores (r[1], ou seja, o segundo índice da matriz, aquela lista com os ganhadores que
            será detalhada na função conferir()).
            """
            if r[0]:
                break

    # Finalizando o jogo
    print(f"Fim do Jogo!\nA(s) cartela(s) ganhadora(s) foram: {r[1]}")


# Função para conferir acertos e caso hajam ganhadores
def conferir(x, y, z, g):
    for l in x:
        for c in range(10):
            # Se o número gerado pelo sorteio for igual ao número presente na cartela, é somado + 1 à pontuação.
            if l[c] == y:
                l[10] += 1
                # Se a pontuação for igual a 10, então a cartela será adicionada à lista de ganhadores (g)
                if l[10] == 10:
                    g.append(x.index(l) + 1)

    # Puxando função de impressão das cartelas
    mostrar_cartelas(x, y, z)
    """
    Caso o tamanho da lista de ganhadores seja maior que 0(ou seja, há pelo menos 1 ganhador), esta função irá retornar uma matriz com o valor de True e uma lista com o(s) ganhador(es). Caso contrário, irá retornar
    uma matriz com uma variável False e uma lista de ganhadores vazia.
    """
    if len(g) > 0:
        res = [True, g]

        return res

    else:
        res = [False, g]

        return res


# Função para exibir as cartelas a medida que os números são sorteados
def mostrar_cartelas(x, y, z):
    sleep(0.5)

    print(f"O último número sorteado foi: {z[len(z) - 2]}")
    sleep(0.5)
    print(f"Todos os números sorteados: {z}")

    sleep(0.5)

    for l in x:
        print(f"Cartela {x.index(l) + 1}: {l[:10]} Pontuação: {l[10]}")

        sleep(0.2)

    print()

    sleep(0.5)

    # Animação dos 3 pontinhos
    for i in range(3):
        print(".", end="")

        sleep(1)

    print("\n")
