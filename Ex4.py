# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def InputValues (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

def ChangeToBinary(numberN: int):
    binaryNumber = ''
    help = False
    if numberN<0:
        numberN*=-1
        help = True
    while numberN > 0:
        binaryNumber = str(numberN % 2) + binaryNumber
        numberN = numberN // 2
    if help is True:
        binaryNumber = "-" + binaryNumber
    return binaryNumber

number = InputValues ("Enter number: ")
print(ChangeToBinary(number))
