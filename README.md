# TechRank
>[!IMPORTANT]
>Es necesario leer todo el README. Contiene información sobre las dependencias necesarias (sin ellas el programa no va a funcionar).

## Introducción
¿Qué es TechRank? TechRank es un proyecto de Web Scraping con Python para ver los lenguajes de programación más utilizados y las noticias más novedosas sobre tecnología. Además, TechRank permite guardar la información en formato .xlsx o .csv. <br>
Además, gracias a JupyterLite, es posible generar imágenes para poder visualizar la información encontrada con el programa y poder visualizarla en dos gráficas. <br> <br>

#### Las imágenes que podemos obtener son las siguientes: <br>
##### Tabla de los lenguajes de programación más utilizados<br>
![image](https://github.com/nmoscatelli/TechRank/assets/118897334/6d5e1fde-f6bb-4a93-9df5-c6fc81477405)<br><br>
##### Tabla de las últimas 10 noticias sobre tecnología<br>
![image](https://github.com/nmoscatelli/TechRank/assets/118897334/153b4681-f6d5-4bb0-bff7-6d3d57d75ae6)<br><br>
##### Gráfico circular de los lenguajes de programación más utilizados<br>
![image](https://github.com/nmoscatelli/TechRank/assets/118897334/ea669151-6b4e-4ecc-bc79-05970a81576b)<br><br>
##### Gráfico de barras de los lenguajes de programación más utilizados<br>
![image](https://github.com/nmoscatelli/TechRank/assets/118897334/65cb2206-b478-4ae5-80c2-f35812233d6e)<br><br>


## Instalación
#### TechRank.py (En consola)
<b> 1. Es necesario tener python instalado.  </b><br> <br>
<b> 2. Descargar las dependencias y librerías de python. </b> <br>
Para ello, hay que copiar en la consola el siguiente comando: <br> 
```bash 
pip install requests beautifulsoup4 pandas openpyxl
```
<b> 3. Acceder y ejecutar el archivo .py</b>  <br>
Para poder ejecutar el archivo .py es necesario utilizar la terminal. Hay que usar el comando `cd` para poder acceder al directorio en el que se encuentra el archivo y luego escribir en la terminal `python techRank.py` para poder ejecutarlo. 

#### TechRank.ipynb
###### Es un archivo NoteBook de JupyterLite
<b> 1. Acceder a JupyterLite </b> <br>
<a href="https://jupyterlite.github.io/demo/lab/index.html"> JupyterLite </a> <br> <br>
<b> 2. Subir los archivos TechRank.ipynb y los archivos que se quieran visualizar en JupyterLite </b>
<b> 3. Abrir el archivo TechRank.ipynb y seguir los pasos </b>

## Tecnologías utilizadas
- Python
- BeautifulSoup
- Pandas
- matplotlib


