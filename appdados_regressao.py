import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfregressao = pd.read_csv('dados_regressao.csv', encoding='latin1')

df = pd.read_csv("dados_regressao.csv")

plt.figure(figsize=(9, 6))
sns.regplot(
    data=df,
    x="renda_mensal",
    y="gasto_mensal",
    scatter_kws={"alpha": 0.6},
    line_kws={"color": "red"}
)

plt.title("Relação entre Renda e Gasto Mensal")
plt.xlabel("Renda Mensal (R$)")
plt.ylabel("Gasto Mensal (R$)")
plt.tight_layout()
plt.show()
