import csv
from typing import Tuple, List, Dict, TextIO #pip3 install typing
from haversine import haversine, Unit #pip3 install haversine
from hospital import Hospital
from farmacia import Farmacia


class DataSetSanitario:
    
    '''
    Crea una clase "DataSetSanitario", que interactua con 2 bases de datos, y las clases
    Hospital y Farmacia. 
    Un DataSetSanitario "d" tiene los atributos:
        - d.farmacias (List[Dict])
        - d.hospitales (List[Dict])
    Y los metodos:
        - d.nombres_de_hospitales
        - d.hospital_por_nombre
        - d.farmacia_mas_cercana
        - d.farmacia_por_hospital
    '''
    
    def __init__(self, farmacias_filename:str, hospitales_filename:str):      
        
        '''
        Requiere: No aparezca mas de una vez el nombre de cada hospital en el archivo .csv.
        Inicializa un DataSet con una lista de farmacias y sus atributos, y una lista
        de hospitales y sus atributos.
        '''
        
        self.farmacias:List[Farmacia] = []
        self.hospitales:List[Hospital] = []
        file_hospitales:TextIO = open(hospitales_filename, 'r', encoding='utf-8')
        linea: Dict[str,str]
        for linea in csv.DictReader(file_hospitales):
            punto:List[float] = (linea['WKT'][7:-1]).split(' ')
            nombre:str = linea['NOM_MAP']
            calle_nombre:str = linea['CALLE']
            calle_altura:int = int(linea['ALTURA'])
            cpa:str = linea['COD_POSTAL']
            hospital:Hospital = Hospital(nombre, calle_nombre, calle_altura, cpa, float(punto[1]), float(punto[0]))
            self.hospitales.append(hospital)
        
        file_farmacias:TextIO = open(farmacias_filename, 'r', encoding='utf-8')
        linea: Dict[str,str]
        for linea in csv.DictReader(file_farmacias):
            
            calle_nombre:str = linea['calle_nombre']
            calle_altura:int = int(linea['calle_altura'])
            cpa:str = linea['codigo_postal_argentino']
            latitud:float = float(linea['lat'])
            longitud:float = float(linea['long'])
            farmacia:Farmacia = Farmacia(calle_nombre, calle_altura, cpa, latitud, longitud)
            self.farmacias.append(farmacia)
        
        file_farmacias.close()
        file_hospitales.close()

    def nombres_de_hospitales(self) -> List:

        ''' 
        Requiere: Nada.
        Devuelve: Una lista con todos los nombres de los hospitales que figuran
        en el archivo subido, ordenados alfabeticamente.
        '''

        lista_de_hospitales:List[str] = []
        for hospital in self.hospitales:
            lista_de_hospitales.append(hospital.nombre) 
        return sorted(lista_de_hospitales)
    
        
    def hospital_por_nombre(self, nombre_ingresado:str) -> Hospital:

        '''
        Requiere: Nombre_ingresado exista en el dataset ingresado.
        Devuelve: El objeto Hospital que coincida con el nombre ingresado.

        '''

        for hospital in self.hospitales:
            if hospital.nombre == nombre_ingresado:
                return hospital
            
    def farmacia_por_hospital(self) -> Dict[Hospital, tuple]:
        
        '''
        Requiere: Nada.
        Devuelve: Un diccionario con un objeto Hospital como clave, y un valor asociado que consiste
        en una tupla con el objeto Farmacia a menor distancia, y la distancia entre ellos.
        '''
        
        hospitales_y_farmacias:Dict[Hospital, Tuple[Farmacia, float]] = {}
        for hospital in self.hospitales:
                respuesta_farmacia: Farmacia = self.farmacia_mas_cercana(hospital)
                distancia:float = respuesta_farmacia.distancia(hospital.latitud, hospital.longitud)
                hospitales_y_farmacias[hospital] = (respuesta_farmacia, distancia)
        return hospitales_y_farmacias
    
    
    def farmacia_mas_cercana(self, hosp:Hospital) -> Farmacia:
        
        '''
        Requiere: Hosp sea un hospital existente en el dataset ingresado.
        Devuelve: El objeto farmacia mas cercano al hospital ingresado.
        '''
        
        farmacia1: Farmacia = self.farmacias[0]
        mejor_distancia: Tuple[Farmacia, float] = (farmacia1, farmacia1.distancia(hosp.latitud, hosp.longitud))
        for farmacia in self.farmacias:
            nueva_distancia:Tuple[Farmacia, float] = (farmacia, farmacia.distancia(hosp.latitud, hosp.longitud))
            if nueva_distancia[1]  < mejor_distancia[1]:
                mejor_distancia = nueva_distancia
        return mejor_distancia[0]
    
d1:DataSetSanitario = DataSetSanitario(farmacias_filename='farmacias_test.csv', hospitales_filename='hospitales_test.csv')
print (d1.farmacia_por_hospital())
