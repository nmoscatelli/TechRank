import requests
from bs4 import BeautifulSoup
import pandas as pd

print("\nBienvenido a TechRank. \n¿Qué quiere revisar?")

data = []

# Input del usuario para decisión
elec = 0
elec = int(input("\n1. Ranking de los lenguajes de programación más utilizados. \n2. Últimas noticias sobre tecnología.\n"))
while (elec != 1 and elec != 2):
    print("\nSeleccione la opción 1 o la opción 2.")
    elec = int(input("1. Ranking de los lenguajes de programación más utilizados. \n2. Últimas noticias sobre tecnología.\n"))

# Lenguajes de programación
if (elec == 1):
    url = "https://www.tiobe.com/tiobe-index/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
        
    table = soup.find("table", class_="table table-striped table-top20")
    rows = table.find_all('tr')
    i = 0
    for row in rows[1:]:
        item = {}
        columns = row.find_all('td')
        item['Rank'] = columns[0].text
        item['Name'] = columns[4].text
        item['Rating'] = columns[5].text
        item['Change'] = columns[6].text
        
        if (int(item['Rank']) < 10): print("0", end="")

        data.append(item)

        print(item['Rank'] + ". " + item['Name'] + ". Rating: " +item['Rating']+ ". Cambio desde el último año: " + item['Change'])
        i = i + 1
        if (i == 10): break

    # Guardar archivo para lenguajes de programación
    elec = str(input("\n¿Quiere guardar los resultados en un archivo .csv o .xlsx? S/N\n"))
    while (elec != "S" and elec != "s" and elec != "N" and elec != "n"):
        print("\nSeleccione S (Si) o N (No).")
        elec = str(input("¿Quiere guardar los resultados en un archivo .csv o .xlsx? S/N\n"))

    if (elec == "S" or elec == "s"):
        elecU = int(input("\n¿En que extensión quiere guardar el archivo?\n1. Extensión .csv\n2. Extensión .xlsx\n3. Cancelar\n "))
        while (elecU != 1 and elecU != 2 and elecU != 3):
            print("\nSeleccione la opción 1 o la opción 2.")
            elecU = int(input("¿En que extensión quiere guardar el archivo?\n1. Extensión .csv\n2. Extensión .xlsx\n3. Cancelar\n"))

        df = pd.DataFrame(data)

        if (elecU == 1):
            df.to_csv("Lenguajes.csv")
            print("Archivo guardado con éxito.")
        elif (elecU == 2):
            try:
                df.to_excel("Lenguajes.xlsx")
                print("Archivo guardado con éxito.")
            except:
                print("Se ha producido un error. Posiblemente no tengas instalado la dependencia necesaria para guardar el archivo en formato excel. Por favor, introduzca en la terminal \"pip install openpyxl\" o siga las instrucciones en GitHub.")

# Noticias
else:
    url = "https://www.nytimes.com/international/section/technology"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    i = 0
        
    news_h3 = soup.find_all("h3", class_="css-1j88qqx e15t083i0")
    newNumber = 0

    for new in news_h3:
        item = {}
        item['Title'] = news_h3[i].text

        if (i < 9): newNumber = "0" + str(i+1)
        else: newNumber = str(i+1)
        print(newNumber + ". " + item['Title'])

        data.append(item)

        i = i +1
        if (i == 10): break
    
    # Guardar archivo para noticias
    elec = str(input("\n¿Quiere guardar los resultados en un archivo .csv o .xlsx? S/N\n"))
    while (elec != "S" and elec != "s" and elec != "N" and elec != "n"):
        print("\nSeleccione S (Si) o N (No).")
        elec = str(input("¿Quiere guardar los resultados en un archivo .csv o .xlsx? S/N\n"))

    if (elec == "S" or elec == "s"):
        elecU = int(input("\n¿En que extensión quiere guardar el archivo?\n1. Extensión .csv\n2. Extensión .xlsx\n3. Cancelar\n "))
        while (elecU != 1 and elecU != 2 and elecU != 3):
            print("\nSeleccione la opción 1 o la opción 2.")
            elecU = int(input("¿En que extensión quiere guardar el archivo?\n1. Extensión .csv\n2. Extensión .xlsx\n3. Cancelar\n"))

        df = pd.DataFrame(data)

        if (elecU == 1):
            df.to_csv("Noticias.csv")
            print("Archivo guardado con éxito.")
        elif (elecU == 2):
            try:
                df.to_excel("Noticias.xlsx")
                print("Archivo guardado con éxito.")
            except:
                print("Se ha producido un error. Posiblemente no tengas instalado la dependencia necesaria para guardar el archivo en formato excel. Por favor, introduzca en la terminal \"pip install openpyxl\" o siga las instrucciones en GitHub.")

print("Aplicación terminada. \nGracias por utilizar TechRank.")        