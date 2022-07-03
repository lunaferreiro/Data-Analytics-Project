from typing import Tuple #pip3 install typing
from haversine import haversine, Unit #pip3 install haversine


class Farmacia:
    
    ''' 
    Crea una clase "Farmacia".
    Un objeto Farmacia 'f' tiene los atributos:
            - f.calle_nombre (str)
            - f.calle_altura (int)
            - f.cpa (int)
            - f.latitud (str)
            - f.longitud (str)
        Y los metodos:
            - f.direccion 
            - f.distancia
    '''
        
    def __init__(self, calle_nombre:str, calle_altura:int, cpa:str, latitud:float, longitud:float):
        
        '''
        Requiere: Nada.
        Inicializa una Farmacia con todos sus atributos.
        
        '''
        
        self.calle_nombre:str = calle_nombre
        self.calle_altura:int = calle_altura
        self.cpa:str = cpa
        self.latitud:float = latitud
        self.longitud:float = longitud


    def direccion(self) -> str:
        
        '''
        Requiere: Nada.

        Devuelve: La concatenacion de strings del nombre de la calle de la farmacia, 
        seguido de su altura y el codigo postal argentino de la farmacia.
        
        '''
        
        return "{} {} ({})".format(self.calle_nombre, self.calle_altura, self.cpa)


      
    def distancia(self, latitud:float, longitud:float) -> float:
        
        '''
        Requiere: Nada.

        Devuelve: La distancia entre la farmacia y el punto dado. 
        
        '''
        
        punto:Tuple[float, float] = (latitud, longitud)
        farmacia = (self.latitud, self.longitud)
        
        return haversine(farmacia, punto, unit=Unit.METERS)


    def __repr__(self):
        
        '''   
        Requiere: Nada.
       
        Devuelve: El formato requerido para cada farmacia en la clase Farmacia. 
        El mismo es la concatenacion de strings del nombre de la calle donde se 
        ubica la farmacia, la altura de la calle y el codigo postal argentino.
        
        '''
        
        return "FARMACIA:{}".format(self.direccion())