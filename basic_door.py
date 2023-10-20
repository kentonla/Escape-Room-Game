from door import Door
import random


class BasicDoor(Door):
    def __init__(self):
        self._state = random.randint(1,2)
        self._input = None

    def examine_door(self):
        return "You encountered a basic door, you can either push it or pull it to open."

    def menu_options(self):
        return ("1. Push\n"
                "2. Pull\n")

    def get_menu_max(self):
        return 2

    def attempt(self, option):
        self._input = option
        choices = ['push', 'pull']
        return f"You {choices[self._input-1]} the door."

    def is_unlocked(self):
        if self._state == self._input:
            return True
        return False

    def clue(self):
        return "Try the other way."

    def success(self):
        # self._input = None
        return "Congratulations, you opened the door.\n"