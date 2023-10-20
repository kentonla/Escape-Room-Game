from door import Door
from random import randint

class ComboDoor(Door):
    def __init__(self) -> None:
        self._correct_value = randint(1,10)
        self._input = None

    def examine_door(self):
        return 'You encounter a door with a combination lock, you can spin the dial to a number 1-10.'
    
    def menu_options(self):
        return 'Enter a number (1-10): '
    
    def get_menu_max(self):
        return 10
    
    def attempt(self, option):
        self._input = option

        return f'You turn the dial to... {self._input}'
    
    def is_unlocked(self):
        return self._input == self._correct_value
    
    def clue(self):
        if  self._input < self._correct_value:
            return 'Try a higher value.'
        elif self._input > self._correct_value:
            return 'Try a lower value.'
        
    
    def success(self):
        # self._input = None
        # self._correct_value = randint(1,10)
        return 'You found the correct value and opened the door.\n'

    
