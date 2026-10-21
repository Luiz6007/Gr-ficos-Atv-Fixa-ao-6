import pandas as pd
import matplotlib.pyplot as plt

dfpizza = pd.read_csv('dados_pizza.csv', encoding='latin1')

df = pd.read_csv("dados_pizza.csv")

plt.figure(figsize=(8, 8))
plt.pie(
    df["faturamento"],
    labels=df["canal_venda"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribuição do Faturamento por Canal de Venda")
plt.axis("equal")
plt.show()
