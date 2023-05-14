class Zasobnik:
    def __init__(self, max_size: int):
        self.zasobnik = []
        self.max_size = max_size
        self.zasobniky = []

    def push(self, item) -> None:
        if (self.size() >= self.max_size):
            pass
        else:
            self.zasobnik.append(item)

    def pop(self) -> None:
        if (len(self.zasobnik) > 0):
            print(self.zasobnik[-1])
            self.zasobnik.pop(-1)
        else:
            pass

    def front(self):
        if (len(self.zasobnik) > 0):
            return self.zasobnik[0]
        else:
            pass

    def rear(self):
        if (len(self.zasobnik) > 0):
            return self.zasobnik[len(self.zasobnik)-1]
        else:
            pass

    def is_empty(self) -> bool:
        if (len(self.zasobnik) <= 0):
            return True
        else:
            return False

    def print_all(self):
        for prvek in self.zasobnik:
            print(prvek)

    def size(self) -> int:
        return len(self.zasobnik)