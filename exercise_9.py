#برنامه ای که اطلاعات کالا را از کاربر میگیرد و قیمت ان راه محاسبه و لیست خرید را نمایش میدهد

my_list =[]
buy = 0
while True:
 mobile = input('enter mobile name :')
 quantity = int(input('qunit of mobiles : '))
 price = int(input('enter price of mobles :'))

 kala = {
    'mobile':mobile,
    'quantity':quantity,
    'price':price
 }
 my_list.append(kala)
 count = quantity * price
 print(f'count:{count}')
 buy = buy + count
 if buy > 1000 :
     break
 else:
     print(f'{buy}$')


for information in my_list:
    print(f"{information['mobile']:5},{information['quantity']:5},{information['price']:10}")

