class Hospital:

    ''' 
    Crea una clase "Hospital".
    Un objeto Hospital 'h' tiene los atributos:
            - h.nombre (str)
            - h.calle_altura (str)
            - h.cpa (str)
            - h.latitud (str)
            - h.longitud (str)
        Y los metodos:
            - h.direccion 
    '''
        
    def __init__(self, nombre:str, calle_nombre:str, calle_altura:int, cpa:str, latitud:float, longitud:float):
       
        '''      
        Requiere: Nada.
        Inicializa una clase "Hospital" con todos sus atributos.
        
        '''
        
        self.nombre:str = nombre
        self.calle_nombre:str = calle_nombre
        self.calle_altura:str = calle_altura
        self.cpa:str = cpa
        self.latitud:str = latitud
        self.longitud:str = longitud     


    def direccion(self) -> str:
        
        '''      
        Requiere: Nada.
        
        Devuelve: La concatenacion de strings del nombre de la calle del hospital, 
        seguido de su altura y el codigo postal argentino del hospital.
        
        '''
        
        return "{} {} ({})".format(self.calle_nombre, self.calle_altura, self.cpa)


    def __repr__(self):
        
        '''   
        Requiere: Nada.
       
        Devuelve: El formato requerido para cada hospital en la clase Hospital. 
        El mismo es la concatenacion de strings del nombre del hospital definido 
        como "nombre" y la funcion direccion.
        
        '''
        
        return "{}--{}".format(self.nombre, self.direccion())