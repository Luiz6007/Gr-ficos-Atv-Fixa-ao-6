import pandas as pd
import matplotlib.pyplot as plt

dflinhas = pd.read_csv('dados_linhas.csv', encoding='latin1')

df = pd.read_csv("dados_linhas.csv")
df["data"] = pd.to_datetime(df["data"])

for loja, dados in df.groupby("loja"):
    dados = dados.sort_values("data")
    plt.plot(dados["data"], dados["vendas"], label=loja)

plt.title("Vendas ao Longo do Tempo por Loja")
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.legend(title="Loja")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
