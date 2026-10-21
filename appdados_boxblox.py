import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfbloxplot = pd.read_csv('dados_boxplot.csv', encoding='latin1')

df = pd.read_csv("dados_boxplot.csv")

plt.figure(figsize=(9, 6))
sns.boxplot(
    data=df,
    x="departamento",
    y="salario"
)

plt.title("Distribuição de Salários por Departamento")
plt.xlabel("Departamento")
plt.ylabel("Salário (R$)")
plt.tight_layout()
plt.show()
