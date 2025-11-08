#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:

class Perceptron:

    def __init__(self, coeficiente_aprendizaje = 0.01, epocas = 50):
        self.funcion_activacion = None
        self.ca = coeficiente_aprendizaje
        self.epocas = epocas
        self.sesgo = None
        self.pesos = None
        
    def set_funcion_activacion(self, funcion):
        self.funcion_activacion = funcion

    def entrenar(self, entradas, salidas):

        muestras = len(entradas)
        if muestras:
            dimension_de_x = len( entradas[0] )
        else:
            dimension_de_x = 0

        self.pesos = [0] * dimension_de_x
        self.sesgo = 0

        #salidas_ = [elemento if elemento == 1 else -1 for elemento in salidas]
        #print(salidas_)

        for epocas in range(self.epocas):
            print(f"{epocas:>2d}","-" * 60)
            contador_de_errores = 0
            for muestra in range(muestras):
                print(self.sesgo, self.pesos)
                sumatoria = sum(xi * wi for xi, wi in zip(entradas[muestra], self.pesos)) + self.sesgo
                resultado = self.funcion_activacion(sumatoria)
                error = salidas[muestra] - resultado
                if error != 0:
                    contador_de_errores += 1
                    for indice, valor in enumerate(entradas[muestra]):
                        self.pesos[indice] += self.ca * error * valor
                    self.sesgo += self.ca * error

            if contador_de_errores == 0:
                break

    def predecir(self, entradas):
        salida = []
        for indice, valor in enumerate(entradas):
                sumatoria = sum(xi * wi for xi, wi in zip(valor, self.pesos)) + self.sesgo
                resultado = self.funcion_activacion(sumatoria)
                salida.append(resultado)
        return salida
