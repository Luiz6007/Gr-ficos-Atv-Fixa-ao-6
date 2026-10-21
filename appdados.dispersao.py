import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfdispersao = pd.read_csv('dados_dispersao.csv', encoding='latin1')

df = pd.read_csv("dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(10, 6))

for barra in ax.patches:
    altura = barra.get_height()
    ax.

plt.title("Relação entre Altura e Peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.legend(title="Grupo")
plt.tight_layout()
plt.show()
