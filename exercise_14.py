class Product:
    """کلاس والد: اطلاعات عمومی کالا"""

    def __init__(self):
        self.name = None
        self.price = None

    def save(self):
        print(f"نام: {self.name}, قیمت: {self.price}")


class ElectricProduct(Product):
    """کالای برقی"""

    def __init__(self):
        super().__init__()
        self.voltage = None

    def save(self):
        print(
            f"نام: {self.name}, قیمت: {self.price}, "
            f"ولتاژ: {self.voltage}"
        )


class NonElectricProduct(Product):
    """کالای غیربرقی"""

    def __init__(self):
        super().__init__()
        self.weight = None

    def save(self):
        print(
            f"نام: {self.name}, قیمت: {self.price}, "
            f"وزن: {self.weight}"
        )


class Laptop(ElectricProduct):
    """لپ‌تاپ"""

    def __init__(self):
        super().__init__()
        self.ram = None
        self.cpu = None

    def save(self):
        print(
            f"نام: {self.name}, قیمت: {self.price}, "
            f"ولتاژ: {self.voltage}, رم: {self.ram}, پردازنده: {self.cpu}"
        )


class Desktop(ElectricProduct):
    """کامپیوتر رومیزی"""

    def __init__(self):
        super().__init__()
        self.ram = None
        self.cpu = None

    def save(self):
        print(
            f"نام: {self.name}, قیمت: {self.price}, "
            f"ولتاژ: {self.voltage}, رم: {self.ram}, پردازنده: {self.cpu}"
        )


class Furniture(NonElectricProduct):
    """مبلمان"""

    def __init__(self):
        super().__init__()
        self.color = None
        self.material = None

    def save(self):
        print(
            f"نام: {self.name}, قیمت: {self.price}, "
            f"وزن: {self.weight}, رنگ: {self.color}, جنس: {self.material}"
        )


# --------------------
# بخش تست کلاس‌ها
# --------------------

laptop1 = Laptop()
laptop1.name = "Laptop"
laptop1.price = 1000
laptop1.voltage = 220
laptop1.ram = "8 GB"
laptop1.cpu = "Core i5"
laptop1.save()

print("-" * 40)

desktop1 = Desktop()
desktop1.name = "Desktop"
desktop1.price = 1500
desktop1.voltage = 220
desktop1.ram = "16 GB"
desktop1.cpu = "Core i7"
desktop1.save()

print("-" * 40)

furniture1 = Furniture()
furniture1.name = "Chair"
furniture1.price = 200
furniture1.weight = 7
furniture1.color = "Brown"
furniture1.material = "Wood"
furniture1.save()
