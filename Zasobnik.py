class Zasobnik:
    def __init__(self, max_size: int):
        self.zasobnik = []
        self.max_size = max_size
        self.zasobniky = []

    def push(self, item) -> None:
        if len(self.zasobnik) <= self.max_size:
            self.zasobnik.append(item)

    def pop(self) -> None:
        if len(self.zasobnik) > 0:
            self.zasobnik.pop()

    def front(self):
        if len(self.zasobnik) > 0:
            return self.zasobnik[0]

    def rear(self):
        if len(self.zasobnik) > 0:
            return self.zasobnik[-1]

    def is_empty(self) -> bool:
        return len(self.zasobnik) == 0

    def print_all(self):
        for prvek in self.zasobnik:
            print(prvek)

    def size(self) -> int:
        return len(self.zasobnik)