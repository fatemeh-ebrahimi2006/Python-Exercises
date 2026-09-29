#برنامه ای بنویسید که تا وقتی کاربر عدد صفر وارد نکرده عدد بگیرد و میانگین عداد فرد دریافتی را چاپ کند
odd_numbers = []
while True:
    num = int(input('Enter a number: '))
    if num == 0 :
        break
    if num % 2 != 0 :
        odd_numbers.append(num)
    else:
        print('enter an odd numer!!!')
odd_numbers.sort()
print(f'odd numbers : {odd_numbers}')
average = sum(odd_numbers)/len(odd_numbers)
print(f'average : {average}')
