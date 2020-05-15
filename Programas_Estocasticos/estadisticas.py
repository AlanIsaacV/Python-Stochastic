import random

class Estadisticas:
    def __init__(self, lista):
        self.lista = lista
        self.mu = self.media()

    def media(self):
        return sum(self.lista) / len(self.lista)

    def varianza(self):
        x_varianza = 0
        for numero in self.lista:
            x_varianza += (numero - self.mu) ** 2
        return round(x_varianza / len(self.lista), 2)

    def desviacion(self):
       return round(self.varianza() ** 0.5, 2)


if __name__ == '__main__':
    # lista = [random.randint(2, 3) for _ in range(100000)]
    lista = [3.1364, 3.124, 3.13, 3.13, 3.1384, 3.1168, 3.1164, 3.132, 3.1208, 3.1548, 3.146, 3.1212, 3.1712, 3.1624, 3.146, 3.1468, 3.154, 3.1076, 3.1512, 3.1468]

    X = Estadisticas(lista)

    # print(f'{X.lista}')
    print(f'Media: \t\t{X.media()}')
    print(f'Varianza: \t{X.varianza()}')
    print(f'Desviacion: \t{X.desviacion()}')