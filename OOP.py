class Banknote:

    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return f"Эта банкнота номиналом {self.value}"

    def __repr__(self):
        return f"Wallet{self.value}"


    def __eq__(self, other):
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        return self.value + other.value


class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0


    def __repr__(self):
        return f"Wallet({self.container})"

    def __contains__(self, item):
        return item in self.container


    def __len__(self):
        return len(self.container)


    def __call__(self):
        return f"{sum(e.value for e in self.container)} rubs"


    def __iter__(self):
        return self


    def __next__(self):
        while 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        raise StopIteration


    def __getitem__(self, item: int):
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key, value):
        if key < 0 or key > len(self.container):
            raise IndexError
        return self.container[key] == value




if __name__ == '__main__':
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred, hundred, fifty)
    print(wallet)


