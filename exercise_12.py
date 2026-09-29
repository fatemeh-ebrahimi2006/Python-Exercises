#برنامه ای بنویسید که تا وقتی کاربر QUIT وارد نکرده اسم بگیرد

names_list = []

while True:
    person_names = input("enter your name : ")

    if person_names.lower() == "quit":
        break
    else:
        names_list.append(person_names)
        print(names_list)
#سسپس اسامی را بر حرب تعداد حروف صدا دار به صورت desc,revers مرتب کنید

names_list.sort(key=lambda names : sum(char in "aeiouAEIOU" for char in names),reverse=True)
print(names_list)

