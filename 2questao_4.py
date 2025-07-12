# Crie uma funcao em Python que receba um numero diga se o numero e par ou impar

def par_ou_impar(nm):

    if nm % 2 == 0:
        return f"O numero e par:{nm}..."
    else:
        return f"Numero e impar:{nm}..."

print(par_ou_impar(5))