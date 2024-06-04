import numpy as np
import matplotlib.pyplot as plt

def menu():
    print("-*" * 22)
    print("1 - Operações com conjuntos")
    print("2 - Operações com funções de segundo grau")
    print("3 - Operações com funções exponenciais")
    print("4 - Operações com matrizes")
    print("5 - Sair")
    print("-*" * 22)
    while True:
        opcaoPrincipal = int(input("Digite a opção escolhida: "))
        if opcaoPrincipal < 1 or opcaoPrincipal > 5:
            print("Número inválido, digite novamente!")
        else:
            break
    return opcaoPrincipal

def conjuntos():
    conjuntoA = []
    conjuntoB = []
    numerosA = input("Digite os valores do conjunto A, separando-os com vírgula: ").split(",")
    numerosB = input("Digite os valores do conjunto B, separando-os com vírgula: ").split(",")
    for valor in numerosA:
        conjuntoA.append(int(valor))
    print (f"O conjunto A é: {conjuntoA}")
    for valor in numerosB:
        conjuntoB.append(int(valor))
    print (f"O conjunto B é: {conjuntoB}")
    return conjuntoA, conjuntoB
def menuConjuntos():
    while True:
        print("--" * 25)
        print("Os conjuntos serão pedidos depois de você escolher a opção!!!")
        print("1 - Verificar se A é subconjunto próprio de B")
        print("2 - Realizar operação de união")
        print("3 - Calcular intersecção")
        print("4 - Calcular diferença")
        print("5 - voltar")
        print("--" * 25)
        opcaoConjunto = int(input("Digite a opção escolhida: "))
        if opcaoConjunto < 1 or opcaoConjunto >  5:
            print("Opção inválida, digite novamente!!!")
        elif opcaoConjunto == 1:
            print("Verificar conjunto")
            verificar_conjuntos()
        elif opcaoConjunto == 2:
            print("Realizar união")
            uniao_conjuntos()
        elif opcaoConjunto == 3:
            print("Calcular intersecção")
            intesecao_conjuntos()
        elif opcaoConjunto == 4:
            print("Calcular diferença")
            diferença_conjuntos()
        elif opcaoConjunto == 5:
            break
        else:
            break
def menu_funcao():
    while True:
        print("--" * 25)
        print("1 - Calcular raízes")
        print("2 - Calcular F(x)")
        print("3 - Calcular vértice")
        print("4 - Gerar gráfico")
        print("5 - voltar")
        print("--" * 25)
        opcaoConjunto = int(input("Digite a opção escolhida: "))
        if opcaoConjunto < 1 or opcaoConjunto >  5:
            print("Opção inválida, digite novamente!!!")
        elif opcaoConjunto == 1:
            print("Calcular raízes")
            a = int(input("Digite o 'a': "))
            b = int(input("Digite o 'b': "))
            c = int(input("Digite o 'c': "))
            raizes_funcao(a,b,c)
        elif opcaoConjunto == 2:
            print("Calcular F(x)")
            x = int(input("Digite o valor de x: "))
            a = int(input("Digite o 'a': "))
            b = int(input("Digite o 'b': "))
            c = int(input("Digite o 'c': "))
            fx_funcao(a,b,c,x)
        elif opcaoConjunto == 3:
            print("Calcular vértice")
            a = int(input("Digite o 'a': "))
            b = int(input("Digite o 'b': "))
            c = int(input("Digite o 'c': "))
            vertice_funcao(a,b,c)
        elif opcaoConjunto == 4:
            a = int(input("Digite o 'a': "))
            b = int(input("Digite o 'b': "))
            c = int(input("Digite o 'c': "))
            grafico_funcao(a,b,c)
        elif opcaoConjunto == 5:
            break
        else:
            break
def menu_exponencial():
    while True:
        print("--" * 25)
        print("1 - Verificar se a função é crescente ou decrescente")
        print("2 - Calcular função em 'x' pedido")
        print("3 - Gerar gráfico")
        print("4 - voltar")
        print("--" * 25)
        opcaoConjunto = int(input("Digite a opção escolhida: "))
        if opcaoConjunto < 1 or opcaoConjunto >  4:
            print("Opção inválida, digite novamente!!!")
        elif opcaoConjunto == 1:
            print("Verificar Crescente ou decrescente")
            verificar_exponencial()
        elif opcaoConjunto == 2:
            print("Calcular valor pedido em X")
            calcular_exponencial()
        elif opcaoConjunto == 3:
            print("Gerar gráfico")
            grafico_exponencial()
        elif opcaoConjunto == 4:
            break
        else:
            break
        
def menu_matrizes():
    while True:
        print("--" * 25)
        print("1 - Verificar se a matriz é quadrada")
        print("2 - Multitplicação de matriz")
        print("3 - Matriz transposta")
        print("4 - voltar")
        print("--" * 25)
        opcaoConjunto = int(input("Digite a opção escolhida: "))
        if opcaoConjunto < 1 or opcaoConjunto >  4:
            print("Opção inválida, digite novamente!!!")
        elif opcaoConjunto >= 1 and opcaoConjunto < 4:
            matriz = []
            numero_linhas_m1 = int(input("Digite o número de linhas: "))
            numero_colunas_m1 = int(input("Digite o número de colunas: "))
            for i in range(0,numero_linhas_m1):
                linhas = []
                for j in range(0, numero_colunas_m1):
                    num = int(input(f"Digite o numero M:{i} x {j}: "))
                    linhas.append(num)
                matriz.append(linhas)
            if opcaoConjunto == 1:
                print("Verificar se a matriz é quadrada")
                verificar_quadrada(numero_linhas_m1, numero_colunas_m1)
            elif opcaoConjunto == 2:
                print("Informações da matriz 2")
                matriz2 = []
                numero_linhas_m2 = int(input("Digite o número de linhas: "))
                numero_colunas_m2 = int(input("Digite o número de colunas: "))
                for c in range(0,numero_linhas_m2):
                    linhas2 = []
                    for d in range(0, numero_colunas_m2):
                        num = int(input(f"Digite o numero M:{c} x {d}: "))
                        linhas2.append(num)
                    matriz2.append(linhas2)
                if numero_colunas_m1 != numero_linhas_m2:
                    print("Erro, essa operação não pode ser continuada")
                else:
                    multiplicacao_matriz(matriz, numero_linhas_m1, numero_colunas_m1, matriz2, numero_linhas_m2, numero_colunas_m2 )
            elif opcaoConjunto == 3:
                matriz_transposta(matriz, numero_linhas_m1, numero_colunas_m1)
        if opcaoConjunto == 4:
            break
        else:
            break

def verificar_quadrada(linhas, colunas): 
    if linhas == colunas:
        print("A matriz é quadrada")
    else:
        print("A matriz não é quadrada")

def multiplicacao_matriz(matriz1, linhasm1, colunasm1, matriz2, linhasm2, colunasm2):
    resultado = []
    
    for i in range(linhasm1):
        linha_resultante = []
        for j in range(colunasm2):
            soma = 0
            for k in range(colunasm1):
                soma += matriz1[i][k] * matriz2[k][j]
            linha_resultante.append(soma)
        resultado.append(linha_resultante)
    print(resultado)

        
def matriz_transposta(matriz, numero_linhas, numero_colunas):
    matriz_t = []
    for j in range(numero_colunas):
        linha_t = []
        for i in range(numero_linhas):
            num = matriz[i][j]
            linha_t.append(num)
        matriz_t.append(linha_t)
    for linha in matriz_t:
        print(linha)
    

def verificar_exponencial():
    a = int(input("Digite o 'a' da função: "))
    b = int(input("Digite o 'b' da função: "))
    if a > 0:
        print(f"A função 'y = {a} x {b} ** x' é  crescente")
    elif a < 0:
        print(f"A função 'y = {a} x {b}²' é  decrescente")
    else:
        print(f"A função 'y = {a} x {b}²' é  neutra")
def calcular_exponencial():
    a = int(input("Digite o 'a' da função: "))
    b = int(input("Digite o 'b' da função: "))
    x = int(input("Digite o 'x' da função: "))
    y = a * b ** x
    print(f"O valor de 'y' para esse x é: {y}" )

def grafico_exponencial():
    a = int(input("Digite o 'a' da função: "))
    b = int(input("Digite o 'b' da função: "))
    x = np.linspace(-10, 10, 400)
    y = a * b ** x
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a} * {b} ** {x}')
    plt.title('Gráfico da Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.show()
    
    
    
def raizes_funcao(a,b,c):
    delta = b**2 -4 * a * c
    if delta >= 0:
        xmais =  (-b + (delta)**(1/2))/(2 * a)
        xmenos =  (-b - (delta)**(1/2))/(2 * a)
        print(f"X1 é : {xmais} \nX2 é {xmenos}")
    else:
        imaginariomais = complex(-b/2 * a, +delta)
        imaginariomenos =  complex(-b/2 * a, - delta)
        print(f"As raízes são complexas e são: X1 é : {imaginariomais} \n X2 é {imaginariomenos}")
        
def fx_funcao(a, b, c, x):
    funcao = a* (x ** 2) + b * x + c
    print(f"O resultado é: {funcao} ")

def vertice_funcao(a, b ,c):
    delta = b**2 -4 * a * c
    x_v = -b / (2 * a)
    y_v = -delta / (4 * a)
    print(f"As cordenadas do vértice x e y são respectivamnte {x_v} e {y_v}")

def grafico_funcao(a,b,c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.title('Gráfico da Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()
    
def verificar_conjuntos():
    conjuntoA, conjuntoB = conjuntos()
    if set(conjuntoA).intersection(conjuntoB) :
        print("Conjunto A é conjunto Próprio de B" )
    else:
        print("Conjunto A não é próprio de B")
def uniao_conjuntos():
    conjuntoA, conjuntoB = conjuntos()
    a = conjuntoA + conjuntoB
    print(f"A união do conjunto A com o conjuto B é: {a}")
def intesecao_conjuntos():
    conjuntoA, conjuntoB = conjuntos()
    interseccao = set(conjuntoA) & set(conjuntoB)
    print(f"A intrsecção de A com B é: {interseccao}")
def diferença_conjuntos():
    conjuntoA, conjuntoB = conjuntos()
    conjunto = set(conjuntoA) - set(conjuntoB)
    print(f"A difereça de A e B é: {conjunto}")
#Código prinpal!!!
while True:
    while True:
        opcaoPrincipal = menu()
        if opcaoPrincipal == 1:
            menuConjuntos()
        elif opcaoPrincipal == 2:
            menu_funcao()
        elif opcaoPrincipal == 3:
            menu_exponencial()
        elif opcaoPrincipal == 4:
            menu_matrizes()
        elif opcaoPrincipal == 5:
            break
        else:
            break
        
    break
print("Acabou")
    




