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

    def test(self):
        print(self.funcion_activacion(-1))

def escalon(valor):
    if valor >= 0:
        return 1
    return 0

def main():
    red = Perceptron()
    red.set_funcion_activacion(escalon)
    entradas = [ [0, 0],
                 [0, 1],
                 [1, 0],
                 [1, 1] ]
    salida = [0,
              0,
              0,
              1]

    red.test()

if __name__ == "__main__":
    main()
