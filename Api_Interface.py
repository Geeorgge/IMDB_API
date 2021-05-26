from abc import abstractmethod, ABC
from Movie import Movie

class ApiConnect(ABC):

    #REDUCIR A UNA SOLA FUNCION PARA OBTENER EL OBJETO -> Movie

    #Regresa un objeto de tipo Movie

    @abstractmethod
    def getMovie(self, nombre:str) -> Movie:
        pass
 
    