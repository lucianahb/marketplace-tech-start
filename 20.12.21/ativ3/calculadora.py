def soma(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        soma = numero1 + numero2
        return soma

def sub(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        sub = numero1 - numero2
        return sub

def multi(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        multi = numero1 * numero2
        return multi

def divi(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        divi = numero1 / numero2
        return divi


def valida_float(numero: float)-> bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f"Valor informado {numero} não é numérico")