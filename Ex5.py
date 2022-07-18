# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def InputValues (text: str):
    check = False
    while not check:
        try:
            number = int(input(f'{text}'))
            check = True
        except ValueError:
            number = int(input(f'{text}'))
    return number

def Fibonachi(number: int):
    i = 0
    firstNumber = secondNumber = 1
    if number <= 1:
        listOfNumbers = [-1, 0, 1]
    else:
        listOfNumbers = [firstNumber, secondNumber]
        copyOfList =[]
        while i < number - 2:
            summPos = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = summPos
            listOfNumbers.append(summPos)
            i += 1
        copyOfList.extend(listOfNumbers)
        listOfNumbers.reverse()
        for j in range(len(listOfNumbers)):
            listOfNumbers[j] = listOfNumbers[j] * -1
        listOfNumbers.append(0)
        listOfNumbers.extend(copyOfList)
    return listOfNumbers #я не думал об оптимизации

number = InputValues('Enter number: ')
print(Fibonachi(number))


