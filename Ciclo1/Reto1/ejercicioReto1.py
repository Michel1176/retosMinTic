def CDT(usuario: str, capital: int, tiempo: int):
    
    if tiempo > 2:
        valorIntereses = (capital * 0.03 * tiempo) / 12
        valorTotal = valorIntereses + capital
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format(usuario, capital, tiempo, valorTotal)
    else:
        valoraPerder = capital * 0.02
        valorTotal = capital - valoraPerder
        return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}" .format(usuario, capital, tiempo, valorTotal)

usuario = input("Digite el nombre de Usuario: ")
capital = int(input("Digite el dinero ingresado al CDT: "))
tiempo = int(input("Digite el tiempo que tiene el CDT: "))

print(CDT(usuario, capital, tiempo))