#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def SumaOfNumbers(ListN: list):
    index = 1
    suma = 0
    while index < len(ListN):
        suma += ListN[index]
        index += 2
    return suma

listOfNumber = [1,2,3,4,5,6,7,8,9,10] 
print(f'List: {listOfNumber}')
print(f'Sum of numbers: {SumaOfNumbers(listOfNumber)}')