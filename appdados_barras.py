import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfbarras = pd.read_csv('dados_boxplot.csv', encoding= 'latin1')

df = pd.read_csv("dados_barras.csv")

plt.title("Vendas Médias por Categoria e Região")
plt.xlabel("Categoria")
plt.ylabel("Vendas Médias")
plt.legend(title="Região")
plt.tight_layout()
plt.show()
