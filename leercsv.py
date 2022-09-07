import csv

with open('news_decline.csv') as csv_file:
    linea=csv_file.readline()  # leer la primera linea
    print(linea)
    print(linea.replace('"','').replace(' ','').replace('\n','').split(","))
    linea2=csv_file.readline() # lee la segunda linea
    print(linea2)
    separado=linea2.split(',')
    print(separado[0].replace('"',''))
    print(float(separado[1].strip()))
    print(float(separado[2].strip()))
    print(float(separado[3].strip(" \n")))
    linea3 = csv_file.readline()
    print(linea3)
    separado=linea3.split(',')
    print(separado[0].replace('"',''))
    print(float(separado[1].strip()))
    print(float(separado[2].strip()))
    print(float(separado[3].strip(" \n")))
    # csv_file.seek(0,0)  # leer archivo en la posicion inicial