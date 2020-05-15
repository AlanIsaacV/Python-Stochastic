import random

class Estadisticas:
    def __init__(self, lista, redondeo):
        self.lista = lista
        self.redondeo = redondeo
        self.mu = self.media()

    def media(self):
        return sum(self.lista) / len(self.lista)

    def varianza(self):
        x_varianza = 0
        for numero in self.lista:
            x_varianza += (numero - self.mu) ** 2
        return round(x_varianza / len(self.lista), self.redondeo)

    def desviacion(self):
       return round(self.varianza() ** 0.5, self.redondeo)


if __name__ == '__main__':
    lista = [random.randint(0, 50) for _ in range(100000)]
    X = Estadisticas(lista)

    # print(f'{X.lista}')
    print(f'Media: \t\t{X.media()}')
    print(f'Varianza: \t{X.varianza()}')
    print(f'Desviacion: \t{X.desviacion()}')