#Напишите программу, которая на вход принимает 5 чисел и находит макс из них
# 1,4,8,7,5 -> 8
# 78, 55, 36,90, 2 ->90
# numbers = [78,55,36,90,2]
# print(numbers)
# max_ = numbers[0]

# for i in numbers:

#     if i > max_:
#         max_ = i

# или

# for i in range(len(numbers)):
#     if numbers[i] > max_:
#         max_ = numbers[i]

# или

a =[]  # a = list()
for _ in range(5):# _ это счетчик, который не используется
    k = int(input('Введите число: ')) 
    a.append(k)   #добавлять в список а k раз

max_ = a[0]
for i in a: #или for i in a[1:]:
    if i > max_:
        max_ = i
   
print(max_)            