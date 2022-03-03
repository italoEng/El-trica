

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
    r = resistencia elétrica em (Ω) \n
    """
    if v == "v":
        resposta = r*i
    elif i == "i":
        resposta = v/r
    else:
        resposta = v/i

    return resposta