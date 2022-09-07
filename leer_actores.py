import csv

listado=[]
with open('actor.csv') as csv_file:
    lector = csv.reader(csv_file, delimiter=",")
    encabezado = next(lector)  # leer el encabezado
    for linea in lector:
        dic={
            "actor_id":float(linea[0]),
            "first_name":linea[1],
            "last_name": linea[2],
            "last_update": linea[3]
        }
        listado.append(dic)

print(listado)

with open('actor_final.csv','w') as csv_file2:
    escritura=csv.writer(csv_file2,delimiter=",",lineterminator='\n')
    for fila in listado:
        print(fila)
        escritura.writerow([
            fila['actor_id'],
            fila['first_name'].capitalize(),
            fila['last_name'].capitalize(),
            fila['last_update']]
        )



