import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Unir todos os dataframes em um único
df_all = pd.concat(dataframes.values(), ignore_index=True)

# Calcular total de vendas por país
sales_by_country = df_all.groupby("delivery_country")["quantity"].sum().reset_index()

# Calcular a idade média dos compradores por país
df_all["buyer_birth_date"] = pd.to_datetime(df_all["buyer_birth_date"], errors="coerce")
df_all["buyer_age"] = datetime.now().year - df_all["buyer_birth_date"].dt.year
avg_age_by_country = df_all.groupby("delivery_country")["buyer_age"].mean().reset_index()

# Criar os gráficos
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Gráfico de total de vendas por país
sns.barplot(data=sales_by_country, x="quantity", y="delivery_country", ax=axes[0], palette="Blues_r")
axes[0].set_title("Total de Vendas por País")
axes[0].set_xlabel("Quantidade Vendida")
axes[0].set_ylabel("País")

# Gráfico da idade média dos compradores por país
sns.barplot(data=avg_age_by_country, x="buyer_age", y="delivery_country", ax=axes[1], palette="Greens_r")
axes[1].set_title("Idade Média dos Compradores por País")
axes[1].set_xlabel("Idade Média")
axes[1].set_ylabel("País")

plt.tight_layout()
plt.show()
