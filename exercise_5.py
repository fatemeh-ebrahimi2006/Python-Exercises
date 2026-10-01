#برنامه ای که تا وقتی کاربر عدد صفر وارد نکرده عدد بگیرد و اعداد زوج و فرد را در دو لیست جداگانه چاپ کند
Even = []
Odd = []

while True :
    number = int(input('Enter a number : '))
    if number == 0 :
        break
    if number % 2 == 0 :
       Even.append(number)
    else:
        Odd.append(number)
Even.sort()
Odd.sort()
print(f'Even numbers : {Even}\nOdd numbers : {Odd}')

