import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler dados
df = pd.read_csv("gasolina.csv")

# Se o CSV tiver colunas com nomes diferentes, ajuste abaixo:
# Exemplo esperado: colunas "dia" e "preco"
if "dia" not in df.columns or "preco" not in df.columns:
    # tenta detectar nomes comuns
    cols = df.columns.tolist()
    print("Colunas detectadas:", cols)
    raise SystemExit("As colunas 'dia' e 'preco' não foram encontradas. Ajuste o CSV.")

# Plot
plt.figure(figsize=(10,5))
sns.lineplot(x="dia", y="preco", data=df, marker="o")
plt.title("Preço médio de venda da gasolina - São Paulo (1 a 10 de Julho de 2021)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)
plt.tight_layout()

# Salvar figura
plt.savefig("gasolina.png", dpi=150)
print("Gráfico salvo como 'gasolina.png'")
