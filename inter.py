import core

def inpuut(pri):
    while True:
        print(pri)
        number = input()
        try:
            float(number)
            num = core.Number(value_dec=number)
            break
        except ValueError:
            if "/" in number:
                drob = number.split("/")
                if drob[1] == "0":
                    print("Некорректное чило")
                    continue
                num = core.Number(nemerator=float(drob[0]), denominator=float(drob[1]))
                break
            print("Введено не число")
    return num



def get_result(num: core.Number):
    print("Результирующие число")
    print("Десятичная дробь: ", num.get_value_dec())
    print("Неправельная дробь: ", num.get_nemerator(),"/",num.get_denominator())


def start_calculator():
    while True:
        cur = input("Введите знак знак (+,-,*,/,^): ")
        if cur == "e": break
        if cur in ("+", "-", "*", "/", "^","**"):
            num1 = inpuut("Введите первое число: ")
            num2 = inpuut("Введите второе число: ")
            if cur == "+":
                num1 + num2
                get_result(num1)
            elif cur == "-":
                num1 - num2
                get_result(num1)
            elif cur == "*":
                num1 * num2
                get_result(num1)
            elif cur == "/":
                num1 / num2
                get_result(num1)
            elif cur == "**" or "^":
                num1 ** num2
                get_result(num1)