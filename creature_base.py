import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

        if self.level < 1:
            raise ValueError("level")

    def get_defensive_roll(self, modifier=3):
        die_roll = random.randint(1, 12)

        return modifier * die_roll * self.level

    def __repr__(self):
        return f"{type(self).__name__}: {self.name} of level {self.level}"


class SmallAnimal(Creature):
    def get_defensive_roll(self, modifier=3):
        base_roll = super().get_defensive_roll(modifier)
        return base_roll / 2


class Wizard(Creature):
    def fight(self, creature):
        print(f"The wizard {self.name} attacks {creature.name}!")

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print(f"You roll {my_roll:,}...")
        print(f"{creature.name} rolls {creature_roll:,}...")

        if my_roll >= creature_roll:
            print(f"The wizard has handily triumphed over {creature.name}")
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False

class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)

        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self, modifier=3):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        # Another sourcery example:
        # is_strong = base_roll or 'Not strong'
        # print(is_strong)

        return int(base_roll * fire_modifier * scale_modifier)