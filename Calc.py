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
    def __init__(self, primeryArg):
        self.primeryArg = primeryArg
    def sum(self, arg: float):
        self.primeryArg += arg

    def multi(self, arg: float):
        self.primeryArg *= arg

    def div(self, arg: float):
        if(arg != 0):
            self.primeryArg /= arg
        else:
            print(f"Ошибка!!! Деление на ноль!")


    def getResult(self) -> float:
        return self.primeryArg