from abc import abstractmethod, ABC
from Movie import Movie

class ApiConnect(ABC):

    #Regresa un objeto de tipo Movie

    @abstractmethod
    def getMovie(self, nombre:str) -> Movie:
        pass
 
    