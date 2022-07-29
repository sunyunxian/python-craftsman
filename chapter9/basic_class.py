i = 1.3
print(i.is_integer())


class Duck:
    def __init__(self, name) -> None:
        self.name = name

    def quack(self):
        print(f"Quack! I'm {self.name}")


donald = Duck('donald')
donald.quack()


class WordyDuck(Duck):
    def quack(self):
        print(f"Quack! Quack! Quack! I'm {self.name}")


wordy_donald = WordyDuck('wordy_donald')
wordy_donald.quack()
