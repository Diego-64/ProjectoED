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
                
    def InfoEquipos(datosliga,equipos):
        
        #def QuienGana(resultado):

        #def Puntos(info):
                    
        #def Clasificacion(datos):

        
        datos=[]
        dict_equipos={}
        
        #Bucle que recorre los nombres de los equipos para crear un diccionario que contengan 
        #los partidos ganados, empatados y perdidos
        for equipo in equipos:
            info={}
            info["Ganados"]=0
            info["Empatados"]=0
            info["Perdidos"]=0
            
            dict_equipos[equipo]=info
           
        #Bucle for que añade puntos en el diccionario de partidos en función de si el equipo
        #ha ganado, perdido o empatado 
        for partido in datosliga:
            local=partido.get("Equipo 1")
            visitante=partido.get("Equipo 2")
            
            resultado=partido.get("FT")
            ganador=QuienGana(resultado)
            
                
            if(ganador==1):
                dict_equipos[local]["Ganados"]+=1
                dict_equipos[visitante]["Perdidos"]+=1
            elif(ganador==0):
                dict_equipos[local]["Empatados"]+=1
                dict_equipos[visitante]["Empatados"]+=1
            elif(ganador==-1):
                dict_equipos[local]["Perdidos"]+=1
                dict_equipos[visitante]["Ganados"]+=1
                     
        #Recorre el diccionario que contiene los equipos y sus partidos para generar los puntos
        #y añadirlos a una lista        
        for clave,valor in dict_equipos.items():
            puntos=Puntos(valor)
            tupla=(clave,valor,puntos)
            datos.append(tupla)
        
        #Devuelve la lista anterior, pero ordenada    
        return Clasificacion(datos)
    #def infoEquipos       

    equipos=Equipos(liga)
    InfoEquipos(liga,equipos)
#def impClasificación

#------------------------------MAIN-------------------------------#    
import csv
liga=[]

liga=leerPartidos()
impClasificacion(liga)

