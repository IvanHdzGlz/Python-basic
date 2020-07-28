# -*- coding: utf-8 -*-

"""
@author: IvanHDZ
LABS
Script que muestra las precios promedios mensuales de la gasolina en México Ene2017-Mayo2020 r1.1
Archivo CSV recuperado de:
https://datos.gob.mx/busca/dataset/ubicacion-de-gasolineras-y-precios-comerciales-de-gasolina-y-diesel-por-estacion/resource/575d6ced-44be-4df6-be2f-c8f6fad84bae
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('dark_background')

#Leyendo Datos
#Para 87 Octanos
df_data = pd.read_csv("DATOS.csv")

#Ploteando
font = {'family': 'sans-serif',
        'color':  'beige', #Aqua para 87octanos
        'weight': 'bold',
        'size': 12,
        }

#Pasando el dataframe a formato extendido, Entidades ahora como columnas
df_wide=df_data.pivot_table(index=["Año_Reporte", "Mes"], columns="Entidad_Federativa", values="Gasolina_Min_87octanos")
df2=df_wide.reset_index()

#agregando filas
df2.index=df2.index*5

#indexando filas nuevas
last_indice = df2.index[-1] + 1
df_exten = df2.reindex(range(last_indice))

#agregando años y meses a nuevas filas
df_exten['Año_Reporte'] = df_exten['Año_Reporte'].fillna(method='ffill')
df_exten['Mes'] = df_exten['Mes'].fillna(method='ffill')
df_exten = df_exten.set_index(['Año_Reporte', 'Mes']) #borrar para poder regresar a formato long

#rankeando en lugar de sort
df_rank_ext = df_exten.rank(axis=1, method='first')

#interpolando datos para nuevas filas
df_exten = df_exten.interpolate()
df_rank_ext = df_rank_ext.interpolate()

#paleta de colores
colores = dict(zip(
    ['Aguascalientes', 'B. C.', 'B.C. Sur', 'Campeche', 'Chiapas', 'Chihuahua', 'CDMX', 'Coahuila', 'Colima', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Michoacán', 'Morelos', 'México', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas'],
    ['aqua', 'red', 'white', 'bisque', 'lime', 'sienna', 'violet', 'plum', 'purple', 'gold', 'azure', 'tan', 'coral', 'hotpink', 'blue', 'royalblue', 'crimson', 'beige', 'teal', 'dodgerblue', 'chartreuse', 'yellow', 'steelblue', 'wheat', 'springgreen', 'fuchsia', 'deeppink', 'magenta', 'indigo', 'turquoise', 'olive', 'orangered']
))
#eje y figura
fig1 = plt.figure(figsize=[13, 5])
ax = fig1.add_subplot(111)

#etiquetas = df_exten.columns
def dibujar_grafica(i):
    ax.clear()
    ax.set_title("Precio promedio mensual por litro de gasolina de 87 Octanos Enero 2017- Mayo 2020 \n en México por entidad federativa", fontdict=font)
    ax.set_xlabel('Precio en pesos mexicanos')
    ax.set_ylabel('Entidad federativa')
    y = df_rank_ext.iloc[i].sort_values(ascending=True).tail(10)
    width = df_exten.iloc[i].sort_values(ascending=True).tail(10)
    etiquetas=y.index
    ax.barh(y=y, width=width, tick_label=etiquetas,color=[colores[x] for x in y.index], edgecolor='gold')
    fecha = df_exten.index[i]
    #limites para gráfica
    low = 12.5
    high = 22
    plt.xlim([low, high])
    
    for k, (width, y) in enumerate(zip(width, y)): 
        ax.text(width + 0.05, y, f'${width:,.2f}', fontsize=8, fontweight='bold', color='lightblue')
    
    ax.text(0.8, 0.07, '{}'.format(fecha), transform=ax.transAxes, size=15, fontweight='bold', ha='left', color='silver')  
    ax.text(0.01, .01, "Datos obtenidos de: https://datos.gob.mx", transform=ax.transAxes, size=9, fontweight='bold', ha='left', color='silver')

animator = animation.FuncAnimation(fig1, dibujar_grafica,frames=len(df_exten), 
                     interval=300, repeat=False)

plt.show()
#animator.save("Interpolado.mp4", fps = None, bitrate = 1800)
#regresando dataframe a formato original
#df3=pd.melt(df_exten, id_vars=["Año_Reporte", "Mes"], value_name='Gasolina_Min_87octanos')
#df3

