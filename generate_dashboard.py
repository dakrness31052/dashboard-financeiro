import pandas as pd
import plotly.graph_objects as go

data = {
    "Mês": ["Maio", "Junho", "Julho", "Agosto"],
    "Receita": [275042.62, 297357.53, 297357.53, 298020.76],
    "Gastos Fixos": [153747.12, 139120.28, 133766.84, 156153.20],
    "Gastos Variáveis": [87837.54, 91810.65, 93743.87, 108708.78],
    "Gastos Sócios": [53416.81, 58716.86, 65716.71, 70348.70],
    "Lucro Líquido": [33457.97, 32709.74, 4130.11, 13158.80]
}

df = pd.DataFrame(data)
print(df)
