import random
from estadisticas import Estadisticas

COORD = [-1, 1]

def aventar_agujas(numero_agujas):
    adentro_circulo = 0

    for _ in range(numero_agujas):
        x = random.random() * random.choice(COORD)
        y = random.random() * random.choice(COORD)

        distancia_centro = (x**2 + y**2)**0.5

        if distancia_centro <= 1:
            adentro_circulo += 1

    return (4 * adentro_circulo) / numero_agujas

def estimacion(numero_agujas, intentos):
    estimados = []
    for _ in range(intentos):
        estimacion_pi = aventar_agujas(numero_agujas)
        estimados.append(estimacion_pi)
    
    concentrado = Estadisticas(estimados, 5)
    print(f'Pi: \t\t{round(concentrado.media(), 5)} \t|')
    print(f'Desviacion: \t{concentrado.desviacion()} \t|')
    print('________________________|')
    return (concentrado.media(), concentrado.desviacion())

def estimar_pi(precision, numero_agujas, intentos):
    sigma = precision
    # Obtiene una distribucion normal de 3 sigmas que es equivalente a una desviacion del 97%
    while sigma >= precision / 3:
        media, sigma = estimacion(numero_agujas, intentos)
        numero_agujas *= 2

    return media

if __name__ == '__main__':
    numero_agujas = int(input('Ingresa el numero de agujas:   '))
    simulaciones = int(input('Numero de simulaciones:   '))
    precision = float(input('Precision:   '))
    estimar_pi(precision, numero_agujas, simulaciones)