

def paralelo(*args):
    """
    função para cálcular resistores em paralelo
    """
    n = len(args) # numero de resistores
    den = 0
    for i in range(n):
        den = 1/args[i-1] + den # denominador
    return 1/den

def lei1(v="v",i="i",r="r"):
    """
    função que cálcula a primeira lei de ohm.\n
    v = tensão elétrica em (V) \n
    i = corrente elétrica em (A) \n
    r = resistencia elétrica em (Ω)
    """
    if v == "v":
        resposta = r*i
    elif i == "i":
        resposta = v/r
    else:
        resposta = v/i

    return resposta

def lei2(r="r",rho ="rho",A="A",L="L"):
    """
    função que cálcula a segunda lei de ohm. \n
    r = resistencia elétrica em (Ω) \n
    ρ = resistividade do condutor (Ω.m) \n
    L = comprimento (m) \n
    A = área da secção transversal (mm²)
    """
    if r == "r":
        resposta = rho*(L/A)
    elif rho == "rho":
        resposta = (r*A)/L
    elif A == "A":
        resposta = (rho*L)/r
    else:
        resposta = (r*A)/rho

    return resposta