import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfdistribuicao = pd.read_csv('dados_distribuicao.csv', encoding='latin1')

df = pd.read_csv("dados_distribuicao.csv")

plt.title("Distribuição das Idades dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Quantidade de Clientes")
plt.tight_layout()
plt.show()
