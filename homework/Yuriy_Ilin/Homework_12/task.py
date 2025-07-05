class Flower:
    def __init__(self, name, color, freshness, stem_length, lifespan, price):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.lifespan = lifespan
        self.price = price

    def __str__(self):
        return (
            f"Цветок: {self.name}, "
            f"цвет: {self.color}, "
            f"свежесть: {self.freshness}/10, "
            f"длина стебля: {self.stem_length} см, "
            f"время жизни: {self.lifespan} дней, "
            f"цена: {self.price} руб."
        )

    def __repr__(self):
        return (
            f"name='{self.name}', "
            f"color='{self.color}', "
            f"freshness={self.freshness}, "
            f"stem_length={self.stem_length}, "
            f"lifespan={self.lifespan}, "
            f"price={self.price}"
        )


class Rose(Flower):
    def __init__(self, color, freshness, stem_length, lifespan, price):
        super().__init__("Роза", color, freshness, stem_length, lifespan, price)


class Lily(Flower):
    def __init__(self, color, freshness, stem_length, lifespan, price):
        super().__init__("Лилия", color, freshness, stem_length, lifespan, price)


class Popy(Flower):
    def __init__(self, color, freshness, stem_length, lifespan, price):
        super().__init__("Мак", color, freshness, stem_length, lifespan, price)


class Bouquet:
    def __init__(self, flowers=None):
        self.flowers = flowers if flowers else []
        self.package_price = 100  # Стоимость упаковки

    def calculate_total_price(self):
        return f"Цена букета: {self.package_price + sum(flower.price for flower in self.flowers)}"

    def time_life(self):
        if not self.flowers:
            return 0
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return f"Срок жизни букета составляет: {int(total_lifespan / len(self.flowers))} дней"

    def sort_bouquet(self, type_sort):
        if type_sort == "color":
            return sorted(self.flowers, key=lambda flower: flower.color)
        elif type_sort == "freshness":
            return sorted(self.flowers, key=lambda flower: flower.freshness)
        elif type_sort == "stem_length":
            return sorted(self.flowers, key=lambda flower: flower.stem_length)
        elif type_sort == "lifespan":
            return sorted(self.flowers, key=lambda flower: flower.lifespan)
        elif type_sort == "price":
            return sorted(self.flowers, key=lambda flower: flower.price)
        else:
            raise ValueError("Указан неверный параметр сортировки!")

    def search_flower(self, parameter):
        if parameter == "color":
            p_color = input('Введите цвет цветка: ')
            result = [flower.name for flower in self.flowers if flower.color == p_color]
            return result if result else 'Цветков с таким цветом в букете не найдено'
        elif parameter == "stem_length":
            p_stem_length = int(input('Введите длину стебля цветка: '))
            result = [flower.name for flower in self.flowers if flower.stem_length == p_stem_length]
            return result if result else 'Цветков с указанной длиной стебля в букете не найдено'
        elif parameter == "price":
            p_price = int(input('Введите стоимость цветка: '))
            result = [flower.name for flower in self.flowers if flower.price == p_price]
            return result if result else 'Цветков с указанной ценой в букете не найдено'

    def __str__(self):
        return (
            f"Количество цветов в букете: {len(self.flowers)}, "
            f"{self.calculate_total_price()} рублей, "
            f"{self.time_life()}"
        )

    def __repr__(self):
        return f"Bouquet(flowers={self.flowers}, package_price={self.package_price})"


white_rose = Rose(color='Белая', freshness=10, stem_length=40, lifespan=14, price=250)
red_rose = Rose(color='Красная', freshness=5, stem_length=40, lifespan=7, price=230)
lily = Lily(color='Белая', freshness=8, stem_length=30, lifespan=6, price=150)
popy = Popy(color='Красный', freshness=10, stem_length=20, lifespan=10, price=100)

bouquet = Bouquet(flowers=[white_rose, red_rose, lily, popy])
print(white_rose)
print(red_rose)
print(lily)
print(popy)
print(bouquet)
