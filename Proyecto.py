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

#funcion impClasificacion()
def impClasificacion(liga):

    def Equipos(datosliga):
        #Se inicia la variable
        lista_equipos=[]
        
        #Bucle for que se encarga de introducir los nombres de los equipos en una lista
        #aparte, revisa que no se añadan nombres repetidos
        for i in datosliga:
            equipo=i.get("Equipo 1")
            if(equipo not in lista_equipos):
                lista_equipos.append(equipo)
                
            equipo=i.get("Equipo 2")
            if(equipo not in lista_equipos):
                lista_equipos.append(equipo)
        
        #Devuelve la lista con los nombres
        return lista_equipos
    #def Equipos
            
    #def InfoEquipos(liga,equipos):

    equipos=Equipos(liga)
    #InfoEquipos(liga,equipos)
    
    
#def impClasificación

#------------------------------MAIN-------------------------------#    
import csv
liga=[]

liga=leerPartidos()
impClasificacion(liga)

