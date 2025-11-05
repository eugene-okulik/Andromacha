class Flowers:
    def __init__(self, name, bud_color, leaves, stem, lifetime, price):
        self.name = name
        self.bud_color = bud_color
        self.leaves = leaves
        self.stem = stem
        self.lifetime = lifetime
        self.price = price

    def __repr__(self):
        return (
            f"Flowers(name='{self.name}', "
            f"bud_color='{self.bud_color}', "
            f"leaves={self.leaves}, "
            f"stem={self.stem}, "
            f"lifetime={self.lifetime}, "
            f"price={self.price})"
        )


class Garden_flowers(Flowers):
    def __init__(self, name, bud_color, leaves, stem, lifetime, fertilizer, price):
        super().__init__(name, bud_color, leaves, stem, lifetime, price)
        self.fertilizer = fertilizer

    def __repr__(self):
        return (
            f"Garden_flowers(name='{self.name}', "
            f"bud_color='{self.bud_color}', "
            f"leaves={self.leaves}, "
            f"stem={self.stem}, "
            f"lifetime={self.lifetime}, "
            f"price={self.price}, "
            f"fertilizer='{self.fertilizer}')"
        )


lily = Garden_flowers("лилия", "white", 1, 40, 7, "yes", 8000)
peony = Garden_flowers("пион", "pink", 2, 10, 5, "yes", 6)


class Wildflowers(Flowers):
    def __init__(self, name, bud_color, leaves, stem, lifetime, habitat, price):
        super().__init__(name, bud_color, leaves, stem, lifetime, price)
        self.habitat = habitat

    def __repr__(self):
        return (
            f"Wildflowers(name='{self.name}', "
            f"bud_color='{self.bud_color}', "
            f"leaves={self.leaves}, "
            f"stem={self.stem}, "
            f"lifetime={self.lifetime}, "
            f"price={self.price}, "
            f"habitat='{self.habitat}')"
        )


poppy = Wildflowers("мак", "red", 3, 3, 9, "луг", 17)
bellflower = Wildflowers("колокольчик", "blue", 4, 1, 15, "поле", 5)


class Bouquet:
    def __init__(self, flowers=None):
        if flowers is None:
            flowers = []
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
            total += f.lifetime
            count += 1
        print(total / count)

    def sort_by(self, parameter):
        self.flowers.sort(key=lambda f: getattr(f, parameter))
        for f in self.flowers:
            print(f.name, getattr(f, parameter))

    def find_by(self, attribute, value):
        found_values = []
        for f in self.flowers:
            if getattr(f, attribute) == value:
                found_values.append(getattr(f, attribute))
        return found_values


my_bouquet = Bouquet([lily, peony, poppy, bellflower])
print(my_bouquet.find_by("bud_color", "red"))
my_bouquet.sort_by("price")
my_bouquet.sort_by("bud_color")
my_bouquet.sort_by("stem")
