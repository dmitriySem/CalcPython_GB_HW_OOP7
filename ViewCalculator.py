from CalculableFactory import ICalculableFactory
class ViewClaculator:
    def __init__(self, calculableFactory):
        self.calculableFactory = calculableFactory

    def run(self):
        while True:
            try:
                primaryArg = int(input("Введите число: "))
            except ValueError:
                print("Вы ввели не число. Повторите ввод")

            calculator = self.calculableFactory.create(primaryArg)

            while True:
                try:
                    arg = float(input("Введите второе число: "))
                    break
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")

            while True:
                cmd = input("Введите команду (+, *, /) : ")
                if (cmd.replace(" ", "") == "+"):
                    calculator.sum(arg)
                    print(calculator.getResult())
                    break
                elif (cmd.replace(" ", "") == "*"):
                    calculator.multi(arg)
                    print(calculator.getResult())
                    break
                elif (cmd.replace(" ", "") == "/"):
                    try:
                        calculator.div(arg)
                        print(calculator.getResult())
                    except ZeroDivisionError:
                        print("Ошибка!!! Деление на ноль!")
                    #
                    break
                #elif (cmd.replace(" ", "") == "="):
                #    calculator.getResult()
                #    break
                else:
                    print("Вы ввели неверную команду, введите (+, *, /)")
            cmd = input("Еще посчитать Да/Нет?")
            if(cmd.replace(" ", "").lower() == "да"):
                continue
            break






