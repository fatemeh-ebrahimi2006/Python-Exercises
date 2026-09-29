#انتخاب واحد
lesson_list = [
    {"name": "Python", "unit": 3, "teacher": "Ahmadi"},
    {"name": "Database", "unit": 3, "teacher": "Mohammadi"},
    {"name": "Math", "unit": 2, "teacher": "Karimi"},
    {"name": "Physics", "unit": 3, "teacher": "Ahmadi"}
]

# گرفتن اطلاعات درس از دانشجو
def get_lesson_info():
    lesson = {
        "name": input("Name: "),
        "unit": int(input("Unit: ")),
        "teacher": input("Teacher: ")
    }

    return lesson

# لیست درس های انتخاب شده توسط دانشجو
selected_list = []

# تعداد درس هایی که دانشجو می خواهد انتخاب کند
count = int(input("How many lessons do you want? (1-4): "))

while count < 1 or count > 4:
    print("Number of lessons must be between 1 and 4")
    count = int(input("How many lessons do you want? (1-4): "))

# انتخاب درس
while len(selected_list) < count:
    selected = get_lesson_info()

    # بررسی معتبر بودن درس انتخاب شده
    result = list(filter(
        lambda lesson:
            lesson["name"].lower() == selected["name"].lower()
            and lesson["unit"] == selected["unit"]
            and lesson["teacher"].lower() == selected["teacher"].lower(),
        lesson_list
    ))

    if result:
        selected_list.append(selected)
        print("Lesson Added!")
        print("Selected Lessons:", selected_list)
    else:
        print("Invalid Lesson!")
        print("Please Try Again")

# مرتب سازی بر اساس تعداد واحد - نزولی
unit_sorted_list = sorted(
    selected_list,
    key=lambda lesson: lesson["unit"],
    reverse=True
)
print("\nLessons Sorted By Unit:")
print(unit_sorted_list)

# مرتب سازی بر اساس نام درس - الفبایی
name_sorted_list = sorted(
    selected_list,
    key=lambda lesson: lesson["name"].lower()
)
print("\nLessons Sorted By Name:")
print(name_sorted_list)

# اضافه کردن قیمت به هر درس
def add_price(lesson):

    if lesson["unit"] == 2:
        lesson["price"] = 1000
    elif lesson["unit"] == 3:
        lesson["price"] = 1500
    return lesson

result = list(map(add_price, selected_list))
print("\nSelected Lessons With Price:")
print(result)

# استخراج قیمت ها
price_list = list(
    map(lambda lesson: lesson["price"], result)
)
print("\nPrice List:")
print(price_list)

# محاسبه مبلغ کل پرداختی
total_price = sum(price_list)
print("\nTotal Price:", total_price)

# تبدیل مبلغ پرداختی به حروف فارسی
from persian_tools import digits
print("Total Price In Words:", digits.convert_to_word(total_price))
