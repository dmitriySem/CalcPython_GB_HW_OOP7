import Calc
import abc


class ICalculableFactory(abc.ABC):
    @abc.abstractmethod
    def create(self, primaryArg: float) -> Calc.ICalculable:
        return Calc.Calculator(primaryArg)


class CalculatorFactory(ICalculableFactory):
    def create(self, primaryArg: float):
        return Calc.Calculator(primaryArg)


