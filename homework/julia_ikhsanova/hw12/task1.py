class Flowers:
    def __init__(self, bud_color, leaves, stem, lifetime, price):
        self.bud = bud_color
        self.leaves = leaves
        self.stem = stem
        self.lifetime = lifetime
        self.price = price


class Garden_flowers(Flowers):
    def __init__(self, bud_color, leaves, stem, lifetime, fertilizer, price):
        super().__init__(bud_color, leaves, stem, lifetime, price)
        self.fertilizer = fertilizer

lily = Garden_flowers("white", 1, 40, 7, "yes", 1000)
peony = Garden_flowers("pink", 2, 10, 5, "yes", 2000)


class Wildflowers(Flowers):
    def __init__(self, bud_color, leaves, stem, lifetime, habitat, price):
        super().__init__(bud_color, leaves, stem, lifetime, price)
        self.habitat = habitat

poppy = Wildflowers("red", 3, 30, 9, "луг", 17)
bellflower = Wildflowers("pink", 4, 40, 15, "поле", 5)


class Bouquet():
    def __init__(self, flowers = []):
        self.flowers = flowers

    def bouquet_price(self):
        total = 0
        for f in self.flowers:
            total += f.price
        print(total)

    def average_lifetime(self):
        total = 0
        count = 0
        for f in self.flowers:
            total = (total + f.lifetime)
            count += 1
        print(total/count)

    # Сортировка цветов по заданному атрибуту
    def sort_flowers(self, attribute):
        flowers_with_values = []
        for f in self.flowers:  #Проходим по всем цветам, которые хранятся в self.flowers
            if attribute == "price":
                value = f.price
            elif attribute == "lifetime":
                value = f.lifetime
            elif attribute == "bud_color":
                value = f.bud
            elif attribute == "leaves":
                value = f.leaves
            elif attribute == "stem":
                value = f.stem
            else:
                continue
            flowers_with_values.append((value, f))
        flowers_with_values.sort(key=lambda x: x[0])
        return [f[1] for f in flowers_with_values]

    # Поиск цветов по заданному атрибуту
    def find_by(self, attribute, value):
        found = []
        for f in self.flowers:
            if hasattr(f, attribute) and getattr(f, attribute) == value:
                found.append(f)
        return found

# my_bouquet = Bouquet([lily, peony, poppy, bellflower])
# my_bouquet.bouquet_price()
# my_bouquet.average_lifetime()
