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
                    arg = int(input("Введите второе число: "))
                    break
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")

            while True:
                cmd = input("Введите команду (+, *, /, =) : ")
                if (cmd.replace(" ", "") == "+"):
                    calculator.sum(arg)
                    continue
                elif (cmd.replace(" ", "") == "*"):
                    calculator.multi(arg)
                    continue
                elif (cmd.replace(" ", "") == "/"):
                    calculator.div(primaryArg)
                    continue
                elif (cmd.replace(" ", "") == "="):
                    calculator.getResult()
                    break
                else:
                    print("Вы ввели не верную команду")
            cmd = input("Еще посчитать Да/Нет?")
            if(cmd.replace(" ", "") == "Да"):
                continue
            break






