import abc
class ICalculable(abc.ABC):

    @abc.abstractmethod
    def sum(self, arg:float):
        pass

    @abc.abstractmethod
    def multi(self, arg:float):
        pass

    @abc.abstractmethod
    def div(self, arg:float):
        pass

    @abc.abstractmethod
    def getResult(self) -> float:
        pass

class Calculator(ICalculable):
    def __init__(self, primeryArg:float):
        self.primeryArg = primeryArg

    def sum(self, arg: float):
        self.primeryArg += arg

    def multi(self, arg: float):
        self.primeryArg *= arg

    def div(self, arg: float):
        #try:
        self.primeryArg = (self.primeryArg / arg)
        #except ZeroDivisionError:


    def getResult(self) -> float:
        return self.primeryArg