#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:

import numpy as np # (1)

from e01_perceptron_01 import Perceptron

# 1. Preparar los datos de la compuerta AND
X_and = np.array([
    [0, 0], 
    [0, 1], 
    [1, 0], 
    [1, 1]
])
y_and = np.array([0, 0, 0, 1])

# 2. Crear y entrenar el modelo Perceptrón
# Unas pocas iteraciones son suficientes para la función AND
perceptron_and = Perceptron(learning_rate=0.1, n_iters=10)
perceptron_and.fit(X_and, y_and)

# 3. Hacer predicciones
predictions_raw = perceptron_and.predict(X_and)

# 4. Convertir las predicciones de -1/1 a 0/1 para la visualización
predictions_01 = np.where(predictions_raw == -1, 0, 1)

# 5. Mostrar los resultados
print("--- Resultados del Perceptrón para la función AND ---")
print("Entradas (X):")
print(X_and)
print("\nSalidas Verdaderas (y):")
print(y_and)
print("\nPredicciones del Perceptrón (0/1):")
print(predictions_01)

# Parámetros aprendidos (Pesos y Sesgo)
print(f"\nPesos finales (w): {perceptron_and.weights}")
print(f"Sesgo final (b): {perceptron_and.bias}")
