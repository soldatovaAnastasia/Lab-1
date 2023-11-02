file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
k1=0
k2=0
for i in range(0, len(list), 2):
    k1+=list[i]
    k2+=list[i+1]
print('Среднее арифметичесоке всех чисел стоящих на четных позициях:' , k1/(len(list)/2))
print('Среднее арифметичесоке всех чисел стоящих на нечетных позициях:' , k2/(len(list)/2))

