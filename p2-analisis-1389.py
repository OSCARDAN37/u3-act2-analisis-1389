# importar librerias
import numpy as np
import pandas as pd
print("Analisis de datos Clientes Oscar Flores NC=1389")
clientes = {
    "Cliente": ["User1", "User2", "User3", "User4", "User5", "User6"],
    "Antiguedad_Meses": [5, 36, 12, 5, 48, 12],
    "Gasto_Mensual": [19.99, 89.99, 59.99, 19.99, 110.00, 59.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}
df = pd.DataFrame(clientes)
print(df)
print("-+-+-+- Agrupar por una sola columna-+-+-+-")
# Agrupar una sola columna
agrupado = df.groupby('Antiguedad_Meses')
print(agrupado)
print("-+-+-+- Promedio por cliente -+-+-+-")
# Promedio de gastos mensuales
print(agrupado['Gasto_Mensual'].mean())
("-+-+-+- Servicios cancelados y aceptados -+-+-+-")
#servicios aceptados
print(agrupado['Cancela_Servicio'].max())

