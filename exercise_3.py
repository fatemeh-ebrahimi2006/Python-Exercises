#میانگین اعداد زوج 3 رقمی بخش پذیر بر 7مجموع اعداد یافت  شده
#مجموع اعداد
sum_number = 0
#تعداد اعداد
count = 0

for i in range (100, 999, 2):
    if i % 7 == 0 :
        sum_number += i    #عددی که شرط در ان بر قرار بود را به مجموع اعداد اضافه کن
        count += 1         #عددی که شرط در ان بر قرار بود را به تعداد اعداد اضافه کن
#شرط میگذاریم برای اینکه بگوییم اگر عددی پیدا شد و count صفر نبود میانگین را اجرا کن
if count != 0 :
    average = sum_number / count
    print(f'the average number is :{average}')

else:
    print('the number is invalid')

