from collections import namedtuple
import csv
from datetime import datetime


Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(rutaCSV:str)->list[Entreno]:
    with open(rutaCSV, mode="r", encoding="utf-8") as r:
        res = []
        lineas = csv.reader(r, delimiter=",")
        next(lineas)
        for campo in lineas:
            tipo = campo[0].strip()
            fechahora = datetime.strptime(campo[1], "%d/%m/%Y %H:%M")
            ubicacion = campo[2].strip()
            duracion = int(campo[3].strip())
            calorias = int(campo[4].strip())
            distancia = float(campo[5].strip())
            frecuencia = int(campo[6].strip())
            compartido = campo[7].upper() == "S"

            res.append(Entreno( tipo, 
                               fechahora, 
                               ubicacion, 
                               duracion, 
                               calorias, 
                               distancia, 
                               frecuencia, 
                               compartido))
        print(res)
    return res
    
lee_entrenos("data/entrenos.csv")

def tipo_entrenos(entrenos:list[Entreno]) -> list[str]:
    tipos:list = set()
    for e in entrenos:
        if(e.tipo not in tipos):
            tipos.add(e.tipo)
    print(tipos)
    return tipos


tipo_entrenos(lee_entrenos("data/entrenos.csv"))

def entrenos_duracion_superior(entrenos:list[Entreno],valor:int)->list[Entreno]:
    lista_entrenos_duracion_mayor:list[Entreno] = list()
    for e in entrenos:
        if(e.duracion >= valor):
            lista_entrenos_duracion_mayor.append(e)
    return lista_entrenos_duracion_mayor

entrenos_duracion_superior(lee_entrenos("data/entrenos.csv"), 50)

def suma_calorias(entrenos:list[Entreno], fecha1:str, fecha2:str)->int:
    calorias_quemadas = 0
    if fecha1 == None or fecha2 == None:
        raise ValueError("Parametro Incorrecto")
    else:
        f1 = datetime.strptime(fecha1, "%d/%m/%Y %H:%M")
        f2 = datetime.strptime(fecha2, "%d/%m/%Y %H:%M")
        for e in entrenos:
            if(f1 >= e.fechahora and  e.fechahora <= f2):
                calorias_quemadas = calorias_quemadas + int(e.calorias)
        return calorias_quemadas

print("Calorias quemadas: "+ str(suma_calorias(lee_entrenos("data/entrenos.csv"), "1/1/2024 8:00", "31/12/2024 8:00")))


    
