#برنامه ای که تا وقتی کاربر کلمه  exit وارد نکرده اسم بگیرد و به ترتیب الفبا یکی یکی چاپ کند
name_list = []

while True:
    names =str(input("Enter name or enter exit to quit : "))
    if names.lower() == "exit" :
        break
    if names.strip():
       name_list.append(names.strip())
    else:
        print("invalid")

name_list.sort()
print(f"{name_list}\nnames in alphabetical: ")
for name in name_list :
    print(name)

