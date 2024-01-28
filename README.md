<p align="center"><img style="width: 300px" src="https://res.cloudinary.com/chaca-sa/image/upload/v1706387034/ouusj9ngzqdfgipq1hcq.webp"/></p>

# 🤮 Proyecto Alex

## 😀 Objetivos

- Intentar sacar 5 en la asignatura y así José sea feliz **(porque yo con un 4 toy happy)**.
- Que Gaby no golpee más al pobre Leandro
- Como siempre rendir tributo a Amaya que ahora mismo debe estar haciendo este baile por no tener que estar dando esta mierda de asignatura.

<p align="center"><img align="center" src="https://res.cloudinary.com/chaca-sa/image/upload/v1682915008/95bc112f-b9d9-44f9-9a29-b8157a92506f_jmkats.webp" style="width: 300px"/></p>

> ### 😹 Chistecillo
> ¿Qué le dice un huevo a una sartén? Me tienes frito.

## 📦 Instalación

> ### ⚠️ Aclaración
>
> El que no utilice PyCharm lo denuncio por mal gusto y crimen contra la humanidad asi que descárguenselo [link de descarga](https://www.jetbrains.com/pycharm/download/?section=windows)

- Crear el entorno virtual con `conda create <nombre_entorno>` o crearlo en el PyCharm directamente
- Instalar los paquetes `rich` y `numpy` en el entorno virtual con `pip install rich` y `pip install numpy`

> ### 😹 Chistecillo
> ¿Cómo se llama el campeón de buceo japonés? Tokofondo. ¿Y el subcampeón? Kasitoko.

## 💻 Tarea 1 (`homework_1`)

En la carpeta `cmd` se encuentran separados por archivos. Así que a continuación me dedico a explicar que hace cada uno de forma muy sensual 😘

### `gen_data`
Este archivo al ejecutarlo va a crear el archivo `data.csv` con datos aleatorios entre los años 2001 y 2023. **Se pueden cambiar todos los valores de la generación en el código** 

### `random_search`
Solución del problema con búsqueda aleatoria. En cada iteración se hacen las siguientes acciones 

- Se generan 5 valores aleatorios de K
- Se calcula el error para esos valores comparandolo con los datos reales
- Si el error es menor al menor error encontrado hasta ese momento se guarda esa solución

### `heuristic_search`
Solución del problema con la función heurística

- Se crean 5 datos aleatorios de K al principio
- Se ejecuta el ciclo
    - Se calcula el error para esos valores comparandolo con los datos reales
    - Si el error es menor al menor error encontrado hasta ese momento se guarda esa solución
    - Si el error es menor a 0 se elige uno de los valores de K de forma aleatoria y se le suma el intervalor indicado (por defecto es 0.1. Se puede cambiar en la clase `KData`) . En caso contrario se suma a ese valor de K el intervalo definido

### `exhaustive_search`
Solución del problema con búsqueda exhaustiva

> ### ⚠️ Aclaración
>
> Esta búsqueda si demora un rato ejecutándose así que tengan paciencia amigos

- Se crean todas las soluciones posibles para el paso
- Se calcula el error con la función objetivo para cada una de las soluciones y se guarda la de menor error

### `all`
Ejecuta todas las búsquedas y muestra los resultados en una tabla. **Se pueden modificar los parámetros de las búsquedas**