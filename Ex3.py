# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

def InputValuesList (text: str):
    check = False
    listForNumbers = []
    while not check:
        try:
            number = float(input(f'{text}'))
            listForNumbers.append(number)
            if len(listForNumbers) == 5:
                check = True
        except ValueError:
            number = float(input(f'{text}'))
    return listForNumbers

def СomparisonOfRealNumbers(listN: list):
    listForComparison = []
    number = ''
    for i in range(len(listN)):
        if listN[i]<0:
            listN[i]*=-1
        lenOfWord = str(listN[i])
        for j in range(len(lenOfWord)):
            if lenOfWord[j] == '.':
                number = '0' + lenOfWord[j:]
                listForComparison.append(number)
                number = ''
    print(listForComparison)
    maxx = float(listForComparison[0])
    minn = float(listForComparison[0])
    for g in range(len(listForComparison)):
        if maxx < float(listForComparison[g]):
            maxx = float(listForComparison[g])
        if minn > float(listForComparison[g]):
            minn = float(listForComparison[g])
    difference = maxx - minn #я не понял как убрать погрешность, ну и не знаю как красивее отделить деситичную часть от целой
    return difference


listOfNumbers = [1.25,2.35,3.45,4.55,5.65,1.02,4.06,6.75,8.80] #InputValuesList ("Enter numbers for list: ")
print(listOfNumbers)
print(СomparisonOfRealNumbers(listOfNumbers))