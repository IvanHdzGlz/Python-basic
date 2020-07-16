# -*- coding: utf-8 -*-

"""
Created on Tue Jun 30 20:44:56 2020
@author: ElMaGo - FR 
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

colores = {'Aguascalientes' : 'aqua',
           'B. C.' : 'red',
           'B.C. Sur' : 'white',
           'Campeche' : 'bisque',
           'Chiapas' : 'lime',
           'Chihuahua' : 'sienna',
           'CDMX' : 'violet',
           'Coahuila' : 'plum',
           'Colima' : 'purple',
           'Durango' : 'gold',
           'Guanajuato' : 'azure',
           'Guerrero' : 'tan',
           'Hidalgo' : 'coral',
           'Jalisco' : 'hotpink',
           'Michoacán' : 'blue',
           'Morelos' : 'royalblue',
           'México' : 'crimson',
           'Nayarit' : 'beige',
           'Nuevo León' : 'teal',
           'Oaxaca' : 'dodgerblue',
           'Puebla' : 'chartreuse',
           'Querétaro' : 'yellow',
           'Quintana Roo' : 'steelblue',
           'San Luis Potosí' : 'wheat',
           'Sinaloa' : 'springgreen',
           'Sonora' : 'fuchsia',
           'Tabasco' : 'deeppink',
           'Tamaulipas' : 'magenta',
           'Tlaxcala' : 'indigo',
           'Veracruz' : 'turquoise',
           'Yucatán' : 'olive',
           'Zacatecas' : 'orangered'}

#Seleccionando conjunto de datos por año y por mes (de 2017 a 2020)
DFacumulador = []
for j in range (4):
    for i in range(12):
        df_Actual = df_data[(df_data['Año_Reporte'] == 2017 + j) & (df_data['Mes'] == i + 1)].sort_values(by='Gasolina_Min_87octanos', ascending=True).tail(10)
        DFacumulador.append(df_Actual)    
        
#Mitigando los DataFrames vacíos
DFacumulador = DFacumulador[:-7]

Enti = DFacumulador[0]
Enti2 = Enti['Entidad_Federativa']

#Ploteando
font = {'family': 'sans-serif',
        'color':  'beige', #Aqua para 87octanos
        'weight': 'bold',
        'size': 12,
        }
#watermark = plt.imread('LogoNECwhite.png')
fig1 = plt.figure(figsize=[13, 5])
ax = fig1.add_subplot(111)
#ax.figure.figimage(watermark, 550, 200, alpha=.4, zorder=1)

def dibujar_grafica(i):
    ax.clear()
    ax.set_title("Precio promedio mensual por litro de gasolina de 87 Octanos Enero 2017- Mayo 2020 \n en México por entidad federativa", fontdict=font)
    ax.set_xlabel('Precio en pesos mexicanos')
    ax.set_ylabel('Entidad federativa')
    ax.barh(DFacumulador[i].Entidad_Federativa, DFacumulador[i].Gasolina_Min_87octanos, color= DFacumulador[i].Entidad_Federativa.replace(colores))
    Año = DFacumulador[i].iloc[1]['Año_Reporte']
    Mes = DFacumulador[i].iloc[1]['Mes']
    #Limites para gráfica de 87 Octanos
    low = 12.5
    high = 22
    plt.xlim([low, high])
    
    
    
    for k,(Gasolina_Min_87octanos, Entidad_Federativa) in enumerate(zip(DFacumulador[i]['Gasolina_Min_87octanos'], DFacumulador[i]['Entidad_Federativa'])):      
        ax.text(Gasolina_Min_87octanos, k, Entidad_Federativa, color='black', fontsize=9, fontweight='bold', ha='right', va='bottom')#para todos los datos usar K-.5, sino K
        ax.text(Gasolina_Min_87octanos+0.1, k, f'${Gasolina_Min_87octanos:}', fontsize=9, fontweight='bold', color='lightblue')
    ax.text(0.89, 0.07, '{}, {}'.format(Mes, Año), transform=ax.transAxes, size=15, fontweight='bold', ha='left', color='silver')  
    ax.text(0.01, .01, "Datos obtenidos de: https://datos.gob.mx", transform=ax.transAxes, size=9, fontweight='bold', ha='left', color='silver')


animator = animation.FuncAnimation(fig1, dibujar_grafica, frames=41, interval=750, repeat=False)
plt.show()

#animator.save('DATOSMAYO2020.mp4', writer="ffmpeg")
animator.save("Gasolina87Octanos.mp4", fps = None, bitrate = 1800)

#plt.tight_layout()
plt.show()

#animator.save('87OctanosMAYO2020.avi', writer="ffmpeg")
#animator.save('91OctanosMAYO2020.mp4', writer="ffmpeg")
#animator.save('DiéselMAYO2020.mp4', writer="ffmpeg")
