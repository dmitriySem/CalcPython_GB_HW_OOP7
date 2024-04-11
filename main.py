import CalculableFactory
import ViewCalculator


if __name__ == '__main__':
    calc = CalculableFactory()
    view = ViewCalculator(calc)
    view.run()


