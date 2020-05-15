import random

def tirar_dado(numero_tiros):
    secuencia_tiros = []
    for _ in range(numero_tiros):
        tiro_1 = random.choice([1,2,3,4,5,6])
        tiro_2 = random.choice([1,2,3,4,5,6])
        secuencia_tiros.append(tiro_1 + tiro_2)
    return secuencia_tiros
    


def main(numero_tiros, numero_simulaciones):
    resultado_simulaciones = []
    for _ in range(numero_simulaciones):
        secuencia_tiros = tirar_dado(numero_tiros)
        resultado_simulaciones.append(secuencia_tiros)

    tiros_con_1 = 0
    for tiro in resultado_simulaciones:
        if 12 in tiro:
            tiros_con_1 += 1
            

    probabilidad_tiros_con_1 = tiros_con_1 / numero_simulaciones
    print(f'La probabilidad de obtener un "12" es:   {probabilidad_tiros_con_1}')

if __name__ == '__main__':
    numero_tiros = int(input('Cuantas veces se va ha tirar el dado:  '))
    numero_simulaciones = int(input('Cuantas simulaciones se va ha ejecutar:  '))

    main(numero_tiros, numero_simulaciones)
