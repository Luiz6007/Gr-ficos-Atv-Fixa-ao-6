import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfheatmap = pd.read_csv('dados_heatmap.csv', encoding='latin1')

df = pd.read_csv("dados_heatmap.csv")

tabela = df.pivot(
    index="dia_semana",
    columns="horario",
    values="movimento_clientes"
)

ordem_dias = [
    "Segunda", "Terça", "Quarta",
    "Quinta", "Sexta", "Sábado", "Domingo"
]
tabela = tabela.reindex(ordem_dias)

plt.figure(figsize=(12, 6))
sns.heatmap(tabela, annot=True, fmt=".0f", cmap="YlOrRd")

plt.title("Movimento de Clientes por Dia e Horário")
plt.xlabel("Horário")
plt.ylabel("Dia da Semana")
plt.tight_layout()
plt.show()
