
#یک عدد بگیر
number = int(input('Enter a number : '))

 #اگر عدد وارد شده مثبت بود از منفی ان عدد تا مثبت ان عدد را چاپ کن
if number > 0 :
    for numbers in range(-number, number+1, 1 ):
        print(numbers)

 #اگر عدد وارد شده منفی بود از مثبت ان عدد تا منفی ان عدد را چاپ کن
elif number < 0 :
    for numbers in range(-number, number-1, -1):
        print(numbers)

 #اگر عدد نه منفی بود و نه مثبت یعنی صفر بود invalid را چاپ کن
else:
    print('invalid')

