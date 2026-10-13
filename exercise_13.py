
class Lesson:
    """اطلاعات درس"""

    def __init__(self):
        self.code = None
        self.name = None
        self.teacher = None
        self.edit = None

    def save(self):
        print(f"Lesson: {self.code}, {self.name}, {self.teacher}")
        if self.edit is not None:
            print(f"New information: {self.edit}")

    def __repr__(self):
        return f"Lesson saved: {self.code}, {self.name}, {self.teacher}, {self.edit}"

    def edit_information(self, new_information):
        self.edit = new_information

#____________________________________________________
#test

lesson1 = Lesson()

lesson1.code = 101
lesson1.name = "Python"
lesson1.teacher = "Ahmad"

lesson1.save()

lesson1.edit_information("Python Advanced")
print()
lesson1.save()


