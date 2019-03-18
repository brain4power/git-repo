from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_stats(self):  # Возвращает итоговые хараетеристики
        # после применения эффекта
        return self.base.get_stats()

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        AbstractEffect.__init__(self, base)
        self.base = base
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_negative_effects()

    def get_stats(self):
        return self.stats.copy()

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append(self.__class__.__name__)
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()


class AbstractNegative(AbstractEffect):
    def __init__(self, base):
        AbstractEffect.__init__(self, base)
        self.base = base
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        self.base.get_stats()

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(self.__class__.__name__)
        return self.negative_effects.copy()


class Berserk(AbstractPositive):
    def __init__(self, base):
        AbstractPositive.__init__(self, base)
        self.base = base
        self.stats = self.base.get_stats()
        self.positive_effects = self.base.get_positive_effects()
        self.negative_effects = self.base.get_positive_effects()

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] += 7
        stats['Endurance'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7

        stats['Perception'] -= 3
        stats['Intelligence'] -= 3
        stats['Charisma'] -= 3
        stats['HP'] += 50

        return stats.copy()

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append(self.__class__.__name__)
        return self.positive_effects

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        return self.negative_effects


class Blessing(AbstractPositive):
    def __init__(self, base):
        AbstractPositive.__init__(self, base)
        self.base = base
        self.stats = base.get_stats()

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] += 2
        stats['Perception'] += 2
        stats['Endurance'] += 2
        stats['Charisma'] += 2
        stats['Intelligence'] += 2
        stats['Agility'] += 2
        stats['Luck'] += 2
        return stats.copy()

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append(self.__class__.__name__)
        return self.positive_effects

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        return self.negative_effects


class Weakness(AbstractNegative):
    def __init__(self, base):
        AbstractNegative.__init__(self, base)
        self.base = base
        self.stats = base.get_stats()

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 4
        stats['Endurance'] -= 4
        stats['Agility'] -= 4
        return stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        return self.positive_effects

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(self.__class__.__name__)
        return self.negative_effects


class EvilEye(AbstractNegative):
    def __init__(self, base):
        AbstractNegative.__init__(self, base)
        self.base = base
        self.stats = base.get_stats()

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        return self.positive_effects

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(self.__class__.__name__)
        return self.negative_effects


class Curse(AbstractNegative):
    def __init__(self, base):
        AbstractNegative.__init__(self, base)
        self.base = base
        self.stats = self.base.get_stats()

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 2
        stats['Perception'] -= 2
        stats['Endurance'] -= 2
        stats['Charisma'] -= 2
        stats['Intelligence'] -= 2
        stats['Agility'] -= 2
        stats['Luck'] -= 2
        return stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        return self.positive_effects

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append(self.__class__.__name__)
        return self.negative_effects


hero = Hero()
print(hero.get_stats())
bers = Berserk(hero)
print(bers.get_stats())