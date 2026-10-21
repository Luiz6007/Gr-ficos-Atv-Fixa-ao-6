import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dffrequencia = pd.read_csv('dados_frequencia.csv', encoding='latin1')

df = pd.read_csv("dados_frequencia.csv")

frequencia = df["tipo_atendimento"].value_counts().reset_index()
frequencia.columns = ["tipo_atendimento", "quantidade"]

plt.figure(figsize=(9, 6))
sns.barplot(
    data=frequencia,
    x="tipo_atendimento",
    y="quantidade"
)

plt.title("Frequência dos Tipos de Atendimento")
plt.xlabel("Tipo de Atendimento")
plt.ylabel("Quantidade")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
