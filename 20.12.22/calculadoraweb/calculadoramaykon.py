def soma(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        soma = numero1 + numero2
        return soma

def subtrai(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        subtrai = numero1 - numero2
        return subtrai

def multiplica(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        multiplica = numero1 * numero2
        return multiplica

def divide(numero1: float, numero2: float) -> float:
    if valida_float(numero1) and valida_float(numero2):
        divide = numero1 / numero2
        return divide



def valida_float(numero: float)-> bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f"Valor informado {numero} não é numérico")