#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
import numpy as np # (1)

class Perceptron: # (2)

    def __init__(self, learning_rate=0.01, n_iters=50): # (3)
        self.lr = learning_rate # (4)
        self.n_iters = n_iters # (5)
        self.activation_func = self._unit_step_func # (6)
        self.weights = None # (7)
        self.bias = None # (8)

    def fit(self, X, y): # (9)
        n_samples, n_features = X.shape # (10)

        # Inicializar pesos y sesgo (bias) (11)
        self.weights = np.zeros(n_features) # (12)
        self.bias = 0 # (13)

        # Reemplazar etiquetas de clase 0 por -1 para el algoritmo (14)
        y_ = np.where(y == 0, -1, 1) # (15)

        # Bucle de entrenamiento (épocas) (16)
        for _ in range(self.n_iters): # (17)
            for idx, x_i in enumerate(X): # (18)

                # Calcular la salida ponderada (producto punto + sesgo) (19)
                linear_output = np.dot(x_i, self.weights) + self.bias # (20)

                # Aplicar función de activación (predicción) (21)
                y_predicted = self.activation_func(linear_output) # (22)

                # Actualizar pesos si hay error (Regla del Perceptrón) (23)
                update = self.lr * (y_[idx] - y_predicted) # (24)
                
                self.weights += update * x_i # (25)
                self.bias += update # (26)

    def predict(self, X): # (27)
        # Calcular la salida ponderada (28)
        linear_output = np.dot(X, self.weights) + self.bias # (29)
        
        # Aplicar función de activación (30)
        y_predicted = self.activation_func(linear_output) # (31)
        return y_predicted # (32)

    def _unit_step_func(self, x): # (33)
        # Función de escalón unitario (34)
        return np.where(x >= 0, 1, -1) # (35)
