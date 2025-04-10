#------------------------------VARIABLES---------------------------#
import csv
liga=[]
#------------------------------FUNCIONES---------------------------#
#Las funciones correspondientes a la primera, segunda parte deben de ir encima,
#al igual que las de la tercera parte, que iran encima de las de la
#segunda parte

#función leerPartidos() 
def leerPartidos():
    partidos=[]
    partido={}
    try:
        with open ("liga.csv") as archivo:
            lector= csv.reader(archivo)
            next(lector)
            for row in lector:
                partido={}
                partido["Fecha"]=row[0]
                partido["Equipo 1"]=row[1]
                partido["Equipo 2"]=row[2]
                partido["FT"]=row[3]
                partido["HT"]=row[4]
                partidos.append(partido)
    except FileNotFoundError:
        print("Ha ocurrido un error al intentar abrir el archivo")
    return partidos


#------------------------------MAIN-------------------------------#    
liga=leerPartidos()
