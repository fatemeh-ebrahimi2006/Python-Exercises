#برنامه ای که از عدد 1تا100 اعداد زوج بخش پذیر بر 7را به صورت لیست چاپ کند
numbers = []
for i in range(0, 101, 2):
    if i % 7 == 0 :
        numbers.append(i)
print(numbers)

