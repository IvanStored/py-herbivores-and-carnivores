class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def remove_dead(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(victim: Animal):
        if isinstance(victim, Herbivore) and not victim.hidden:
            victim.health -= 50
            victim.remove_dead()
