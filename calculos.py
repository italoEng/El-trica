

def paralelo(*args):
    """
    função para calcular resistores em paralelo
    """
    n = len(args) # numero de resistores
    den = 0
    for i in range(n):
        den = 1/args[i-1] + den # denominador
    return 1/den