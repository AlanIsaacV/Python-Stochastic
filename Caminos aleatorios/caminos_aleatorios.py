from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(nombre = 'David')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simularcion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simularcion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia recorrida')
    grafica.line(x,y, legend_lable='Distancia media')

    show(grafica)

def main(distancias_caminata, numero_intentos, tipo_borracho):
    distancia_media_caminata = []

    for pasos in distancias_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)

        distancia_media_caminata.append(distancia_media)

        print(f'{tipo_borracho.__name__} caminata aleatoria de  {pasos}')
        print(f'Media :  {distancia_media} ')
        print(f'Maxima :  {distancia_maxima} ')
        print(f'Minima :  {distancia_minima} ')

    graficar(distancia_caminata, distancia_media_caminata)

if __name__ == '__main__':
    distancias_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100

    main(distancias_caminata, numero_intentos, BorrachoTradicional)