import csv

listado = [] # creamos un listado vacio

with open('news_decline.csv') as csv_file:
    lector = csv.reader(csv_file, delimiter=",")
    encabezado = next(lector)  # leer el encabezado
    for linea in lector:  # lee las lineas siguientes (despues del encabezado
        print(linea[0], linea[1], linea[2], linea[3])
        dic = {  # crea un diccionario con los datos de cada columna
            "show": linea[0],
            "2009": float(linea[1].strip()),
            "2010": float(linea[2].strip()),
            "2011": float(linea[3].strip())}
        listado.append(dic)  # y agregar el diccionario a la lista

print(listado[1:])  # quito la primera fila.
