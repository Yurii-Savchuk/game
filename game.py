from abc import ABC, abstractmethod
import random


class Unit(ABC):
    _name = None
    _health = 100
    _dmg = 1
    _defence = 10
    _chance = 10
    _evasion = 10

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def _get_dmg(self):
        pass

    @abstractmethod
    def _get_defence(self):
        pass

    def _check_health(self, enemy):
        if enemy._health < self._dmg:
            enemy._health -= enemy._health
        elif enemy._health == 0:
            raise Exception('You can\`t attack cadaver!')

    def _get_evasion(self, enemy):
        rand = random.randint(1, 100)
        while True:
            if rand <= self._evasion:
                yield enemy._get_dmg * 0
            else:
                yield enemy._get_dmg


class Mage(Unit):

    def __init__(self, name, dmg, defence, health):
        self._name = name
        self._dmg = dmg
        self._defence = defence
        self._health = health

    def _get_dmg(self):
        self._dmg = _dmg
        # _dmg will depend on equipment
        rand = random.randint(1, 100)
        while True:
            if rand <= Unit._chance:
                yield _dmg * 2
            else:
                yield _dmg

    def _get_defence(self):
        self._defence = _defence
        # _defence will depend on equipment
        return self._defence

    def attack(self, enemy):
        if not isinstance(enemy, Unit):
            raise Exception('You can attack only enemy!')

        _dmg = self._get_dmg()
        _defence = enemy._get_defence()
        _evasion = enemy._get_evasion()
        enemy._health -= _defence - _evasion


class Knight(Unit):

    def __init__(self, name, dmg, defence, health):
        self._name = name
        self._dmg = dmg
        self._defence = defence
        self._health = health

    def _get_dmg(self):
        self._dmg = _dmg
        # _dmg will depend on equipment
        rand = random.randint(1, 100)
        while True:
            if rand <= Unit._chance:
                yield _dmg * 2
            else:
                yield _dmg

    def _get_defence(self):
        self._defence = _defence
        # _defence will depend on equipment
        return self._defence

    def attack(self, enemy):
        if not isinstance(enemy, Unit):
            raise Exception('You can attack only enemy!')

        _dmg = self._get_dmg()
        _defence = enemy._get_defence()
        _evasion = enemy._get_evasion()
        enemy._health -= _defence / 2 - _evasion


class Abillities(Mage):
    _dmg = Mage._dmg
    _defence = Mage._defence
    fireball = _dmg * 2
    frost_armour = _defence * 1.5
    attack_count = 0

    def mage_attack(self, attack_count=0):
        while Mage.attack():
            attack_count += 1
            if attack_count // 3:
                Abillities.fireball
            elif attack_count // 4:
                Abillities.frost_armour
            else:
                Mage.attack()


class Stuff:
    _char = None
    _item_name = None
    _health = 100
    _dmg = 1
    _defence = 10

    def __init__(self, char, item_name, dmg, defence, health):
        self.char = char
        self._item_name = item_name
        self._dmg = dmg
        self._defence = defence
        self._health = health

    def check_char_class(self, char):
        if isinstance(char, Mage):
            self._dmg = dmg
            self._defence = defence
            self._health = health
            return Mage._dmg + dmg, Mage._defence + defence, Mage._health + health
        elif isinstance(char, Knight):
            self._dmg = dmg
            self._defence = defence
            self._health = health
            return Knight._dmg + dmg, Knight._defence + defence, Knight._health + health



class Battle:
    modifications = {
        Mage: {
            '_dmg': 2,
            '_defence': 1,
            '_health': 4},
        Knight: {
            '_dmg': 2,
            '_defence': 1,
            '_health': 4}
    }

    def __init__(self, unit1, unit2):
        if not isinstance(unit1, Unit) or not isinstance(unit2, Unit):
            raise Exception

        # self.units = (unit1, unit2)
        self.unit1 = unit1
        self.unit2 = unit2

    def set_mods_into_battle(self, location=None, daypart=None):
        return self.modifications


    def deploy_mods_into_unit(self, unit):
        key = unit.__class__
        mods = self.modifications[key]

        for i in mods:
            attr = getattr(unit, i, None)

            if isinstance(attr, (int, float)):

                val = attr + mods[i]
                setattr(unit, i, val)

        return unit

    def decide_first(self):

        arr = random.shuffle([self.unit1, self.unit2])
        return arr

    def do_battle(self):
        self.unit1 = self.deploy_mods_into_unit(self.unit1)
        self.unit2 = self.deploy_mods_into_unit(self.unit2)
        lst = self.decide_first()
        self.unit1 = lst[0]
        self.unit2 = lst[1]

        while True:
            self.unit1.attack(self.unit2)
            if self.unit2._hp <= 0:
                return self.unit1

            self.unit2.attack(self.unit1)
            if self.unit1._hp <= 0:
                return self.unit2



u1 = Knight('Bob', 100, 10, 10)
u2 = Mage('Clint', 100, 10, 10)
Battle(u1, u2)