# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:45:00 2020

@author: ivanc
"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('dark_background')

df= pd.read_csv('DATOS.csv')

font = {'family': 'sans-serif',
        'color':  'beige', #Aqua para 87octanos
        'weight': 'bold',
        'size': 12,
        }

colores = dict(zip(
    ['Aguascalientes', 'B. C.', 'B.C. Sur', 'Campeche', 'Chiapas', 'Chihuahua', 'CDMX', 'Coahuila', 'Colima', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Michoacán', 'Morelos', 'México', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas'],
    ['aqua', 'red', 'white', 'bisque', 'lime', 'sienna', 'violet', 'plum', 'purple', 'gold', 'azure', 'tan', 'coral', 'hotpink', 'blue', 'royalblue', 'crimson', 'beige', 'teal', 'dodgerblue', 'chartreuse', 'yellow', 'steelblue', 'wheat', 'springgreen', 'fuchsia', 'deeppink', 'magenta', 'indigo', 'turquoise', 'olive', 'orangered']
))

fig = plt.figure(figsize=[15, 8])
ax = fig.add_subplot(111)
#fig, ax = plt.subplots(figsize=(15, 8))
def racing_barchart(Año):
    ax.clear()
    for i in range(12):
        dff = df[(df['Año_Reporte'].eq(Año)) &(df['Mes'].eq(i+1))].sort_values(by='Gasolina_Min_87octanos', ascending=True)
    ax.set_title('Precio promedio mensual por litro de gasolina de 87 Octanos Enero 2017- Mayo 2020 \n en México por entidad federativa')
    ax.set_xlabel('Precio en pesos mexicanos')
    ax.set_ylabel('Entidad federativa')
    ax.barh(dff['Entidad_Federativa'], dff['Gasolina_Min_87octanos'], color=[colores[x] for x in dff['Entidad_Federativa']])
    dx = dff['Gasolina_Min_87octanos'].max() / 12
    low = 12.5
    high = 22
    plt.xlim([low, high])

    for k, (Gasolina_Min_87octanos, Entidad_Federativa) in enumerate(zip(dff['Gasolina_Min_87octanos'], dff['Entidad_Federativa'])):
        ax.text(Gasolina_Min_87octanos-dx, k-.5, Entidad_Federativa, color='black', fontsize=9, fontweight='bold', ha='right', va='bottom')#para todos los datos usar K-.5, sino K
        #ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(Gasolina_Min_87octanos+.05, k, f'${Gasolina_Min_87octanos:}', fontsize=9, ha='left',  va='center')
    
    ax.text(0.89, 0.07, '{}, {}'.format(i+1, Año), transform=ax.transAxes, color='silver', size=15, ha='left', fontweight='bold')
    ax.text(0.01, .01, "Datos obtenidos de: https://datos.gob.mx", transform=ax.transAxes, size=9, fontweight='bold', ha='left', color='silver')
    ax.set_axisbelow(True)
    plt.box(False)

animator = animation.FuncAnimation(fig, racing_barchart, frames=range(2017, 2020))
#animator.save("GasolinaA.mp4", fps = None, bitrate = 1800)