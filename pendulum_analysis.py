import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
sns.set_theme()

# Lê o arquivo CSV com os dados
df = pd.read_csv("data.csv")
df = df[10:]  # Remove os primeiros 10 pontos para evitar ruído inicial

# Normaliza a coluna 'x' entre -1 e 1
df["x"] = (np.max(df["x"]) + np.min(df["x"])) / 2
df["x"] = 2 / (np.max(df["x"]) - np.min(df["x"]))

# Converte a escala de 'x' para metros com base na amplitude real (em cm)
amplitude = 22  # A amplitude real deve ser definida aqui
df["x"] *= (amplitude/2) / 100  # Converte de cm para metros

# Função modelo para ajuste: oscilação amortecida
def func(t, a, b, w, phi):
    # x(t) = A e^{-bt}cos(wt - phi)
    return a * np.exp(-b * t) * np.cos(w * t - phi)

# Realiza o ajuste da curva (fit) para os dados
popt, _ = curve_fit(func, df["t"], df["x"])
df["fit"] = func(df["t"], *popt)  # Adiciona os valores ajustados ao DataFrame

# Plota os dados e o ajuste
sns.scatterplot(df, x="t", y="x", label="Pontos Amostrais")
sns.lineplot(df, x="t", y="fit", label=f"Fit, a = {popt[0].round(2)}, b = {popt[1].round(2)}, w = {popt[2].round(2)}, phi = {popt[3].round(2)}")
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("x(t)")
plt.legend(loc="best")
plt.show()

# Calcula o período e o fator de qualidade (Q) e salva os resultados em um arquivo de texto
with open("resultados.txt", "w+") as file:
    period = 2 * np.pi / popt[2]  # Período da oscilação
    quality = 2 * np.pi / (1 - np.exp(-2 * popt[1] * period))  # Fator de qualidade (Q)
    file.write(f"Fator de Qualidade: {quality}")
