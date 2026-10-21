import subprocess
import sys
import os

# Menu principal dos gráficos
graficos = {
    "1": ("Heatmap", "appdados_heatmap.py"),
    "2": ("Gráfico de Linhas", "appdados_linhas.py"),
    "3": ("Gráfico de Pizza", "appdados_pizza.py"),
    "4": ("Regressão", "appdados_regressao.py"),
    "5": ("Gráfico de Barras", "appdados_barras.py"),
    "6": ("Boxplot", "appdados_boxplot.py"),
    "7": ("Dispersão", "appdados_dispersao.py"),
    "8": ("Distribuição", "appdados_distribuicao.py"),
    "9": ("Frequência", "appdados_frequencia.py")
}


def menu():
    while True:
        print("\n" + "=" * 40)
        print("       SISTEMA DE GRÁFICOS")
        print("=" * 40)

        for numero, (nome, arquivo) in graficos.items():
            print(f"{numero} - {nome}")

        print("0 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Programa encerrado!")
            break

        if opcao not in graficos:
            print("Opção inválida! Tente novamente.")
            continue

        nome, arquivo = graficos[opcao]

        # Localiza o arquivo na mesma pasta do app.py
        caminho = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            arquivo
        )

        if not os.path.isfile(caminho):
            print(f"Erro: arquivo '{arquivo}' não encontrado!")
            continue

        print(f"\nAbrindo {nome}...")

        try:
            subprocess.run(
                [sys.executable, caminho],
                check=False
            )
        except Exception as erro:
            print(f"Erro ao executar o gráfico: {erro}")

        input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    menu()
