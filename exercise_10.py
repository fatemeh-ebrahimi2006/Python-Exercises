#برنامه انتخاب واحد به شرطی که بیشتر از 17 واحد انتخاب واحد انجام نشود

lesson_list = []
count = 0

while True :
    title = input('enter title lessons : ')
    teacher = input('enter teachers full name: ')
    duration = int(input('enter time of duration: '))
    unit = int(input('enter how many unit you have to pass'))
    count += unit

    if unit > 17 :
        break
    infor = {
        'title':title,
        'teacher':teacher,
        'unit':unit
    }
    lesson_list.append(infor)

for lesson in lesson_list:
    print(f"{lesson['title']:10},{lesson['teacher']:10},{lesson['unit']}")

