from datetime import datetime


fecha= datetime.now()
print(fecha)
print(fecha.month)

texto="30/12/2020"
fecha=datetime.strptime(texto,"%d/%m/%Y")
print(fecha)

print(f"El año: {fecha.year}, mes: {fecha.month}, dia:{fecha.day}")

listado=texto.split('/')
print(f"El año: {listado[2]}, mes: {listado[1]}, dia:{listado[0]}")

