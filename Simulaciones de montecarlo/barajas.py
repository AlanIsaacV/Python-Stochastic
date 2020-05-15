import random
import collections

PALOS = ['corazon', 'peca', 'trebol', 'diamante']
CARTAS = ['a', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'j', 'q', 'k']

def crear_baraja():
    baraja = []
    for palo in PALOS:
        for carta in CARTAS:
            baraja.append((palo, carta))
    return baraja

def obtener_mano(baraja, tamano_mano):
    mano = random.sample(baraja, tamano_mano)
    return mano

def main(tamano_mano, intentos):
    baraja = crear_baraja()
    manos = []
    
    for _ in range(intentos):
        mano = obtener_mano(baraja, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        contador = dict(collections.Counter(valores))
        for valor in contador.values():
            if valor == 2:
                pares += 1
                break

    probabilidad_par = (pares / intentos) * 100
    print(f'La probabilidad de obtener un par en una mano de  {tamano_mano} cartas es de: \t{probabilidad_par}%')


if __name__ == '__main__':
    tamano_mano = int(input('Tamaño de la mano:    '))
    intentos = int(input('Numero de imulaciones:   '))
    main(tamano_mano, intentos)