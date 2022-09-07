import csv

listado=[]

with open('news_decline.csv') as csv_file:
    lector=csv.reader(csv_file,delimiter= ",")
    for linea in lector:
        print(linea[0],linea[1],linea[2],linea[3])
        listado.append({
            "show":linea[0],
            "2009":float(linea[1].strip()),
            "2010":float(linea[2].strip()),
            "2011":float(linea[3].strip())})

print(listado[1:]) # quito la primera fila.



