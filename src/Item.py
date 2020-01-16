class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"\nYou picked up the {self.name}")
        print(f"\n** {self.description} **")

    def on_drop(self):
        print(f"\nYou just dropped the {self.name}")

    def __repr__(self):
        return self.name