# Baixe o arquivo clientes.csv 
# Nota: Utilize o Jupyter ou o Google Colab.
# Nota: Apenas fictício.

# Passo a Passo 

# Passo 1: Importar a base de dados 
import pandas as pd 
import plotly.express as px

tabela = pd.read_csv("clientes.csv", encoding = "latin", sep = ";")
# Entender as informações que você tem disponível
# Procurar erros na base de dados 

# Passo 2: Visualizar a base de dados 

# Deletar a coluna inútil 

# axis = 0 - se for linha ; axis = 1 se for coluna
tabela = tabela.drop("Unnamed: 8", axis = 1)
print(tabela)

# Passo 3: Tratamento de dados

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors = "coerce")

# Acertar informações que estão sendo reconhecidas de forma errada
tabela = tabela.dropna()
# Corrigir informações vazias 
print(tabela.info())

# Passo 4: Análise Inicial -> entender as notas dos clientes 

print(tabela.describe())

# Passo 5: Análise Completa -> Entender cada características do cliente impacto na nota 

# Crie o gráfico
for coluna in tabela.columns:
  grafico = px.histogram(tabela, x = coluna, y = "Nota (1-100)", histfunc = 'avg', text_auto = True, nbins = 10)
# Exibe o gráfico
  grafico.show() 

# Perfil ideal do cliente 
# Acima de 15 anos (Não possui diferenças entre as faixas etárias)
# Faixa salarial parece não fazer diferença 
# Áreas de trabalho: Entretenimento e Artista (Evitar Construção)
# Tem entre 10 a 15 anos de experiência de trabalho 
# Com famílias não tão grande (Máximo 7 pessoas).
