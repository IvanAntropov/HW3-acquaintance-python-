# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def MultiOfNumbers(ListN: list):
    multi = 0
    j = 1
    listForPrint = []
    rangeForLoop = int(len(ListN)/2)
    for i in range(rangeForLoop):
        multi = ListN[-j] * ListN[i]
        listForPrint.append(f'{i+1} pair of {ListN[-j]}*{ListN[i]} = {multi} ') 
        if rangeForLoop < len(ListN)/2 and i == rangeForLoop - 1:
            multi = ListN[int(len(ListN)/2)]**2 
            listForPrint.append(f'{i+2} pair of {ListN[int(len(ListN)/2)]}*{ListN[int(len(ListN)/2)]} = {multi} Я не знаю что делать с такими парами, так что я просто возвожу в квадрат.') 
        j+=1
    return listForPrint
    
listOfNumber = [1,2,3,4,5,6,7,8,9,10,11] 
print(f'List: {listOfNumber}')
for i in range(len(MultiOfNumbers(listOfNumber))):
    ForPrint = MultiOfNumbers(listOfNumber)
    print(ForPrint[i])
