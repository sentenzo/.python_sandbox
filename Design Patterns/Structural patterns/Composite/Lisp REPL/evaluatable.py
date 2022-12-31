from abc import ABC, abstractmethod

class Evaluatable(ABC): # component
    @abstractmethod
    def eval(self) -> any: pass