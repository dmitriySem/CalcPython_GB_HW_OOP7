import CalculableFactory
import ViewCalculator




if __name__ == '__main__':
    calc = CalculableFactory.CalculatorFactory()
    view = ViewCalculator.ViewClaculator(calc)
    view.run()



