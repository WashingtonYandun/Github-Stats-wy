import matplotlib.pyplot as plt

# Datos: nombres de las categorías y sus respectivos valores
labels = ['Python', 'JavaScript', 'C#', 'Java', 'C++']
sizes = [25, 30, 15, 20, 10]

# Colores personalizados para cada sección del pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Explode (destacar) la 1ra y 4ta porción
explode = (0.1, 0, 0, 0.1, 0)

fig1, ax1 = plt.subplots()

# Pie chart con configuraciones adicionales
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)

# Añadir un círculo al centro para convertirlo en un gráfico de dona
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Igualar la relación de aspecto para que se vea como un círculo
ax1.axis('equal')  

# Mejoras estéticas: título y configuración del texto
plt.title('Distribución de Uso de Lenguajes de Programación en 2024', pad=20)
plt.setp(ax1.texts, fontweight=600, color='black')

plt.show()
