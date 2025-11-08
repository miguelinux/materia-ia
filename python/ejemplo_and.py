#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:

from perceptron import Perceptron

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

    red.entrenar(entradas, salida)
    res = red.predecir(entradas)
    print("*" * 60)
    print(res, "=", salida)

    red.graficar_linea(entradas)

if __name__ == "__main__":
    main()
