from door import Door
import random


class DeadboltDoor(Door):
    def __init__(self):
        self._bolt1 = random.choice([True, False])
        self._bolt2 = random.choice([True, False])

    def examine_door(self):
        return ("You encounter a double deadbolt door, \n"
                "both deadbolts must be unlocked to open it, \n"
                "but you can't tell from looking at them whether they're locked or unlocked.\n")

    def menu_options(self):
        return (f"1. Toggle bolt 1\n"
                "2. Toggle bolt 2\n")

    def get_menu_max(self):
        return 2

    def attempt(self, option):
        if option == 1:
            if self._bolt1:
                self._bolt1 = False
            else:
                self._bolt1 = True
        if option == 2:
            if self._bolt2:
                self._bolt2 = False
            else:
                self._bolt2 = True
        choices = ['first', 'second']
        return f"You toggled the {choices[option - 1]} bolt."

    def is_unlocked(self):
        if self._bolt1 and self._bolt2:
            return True
        return False

    def clue(self):
        if self._bolt1 and self._bolt2:
            pass
        elif (self._bolt1 and not self._bolt2) or (self._bolt2 and not self._bolt1):
            return "You jiggle the door... it seems like one of the bolts is unlocked."
        else:
            return "You jiggle the door... it's completely locked."
        return "Try the other way."

    def success(self):
        # self._bolt1 = random.choice([True, False])
        # self._bolt2 = random.choice([True, False])
        return 'You unlocked both deadbolts and opened the door\n'
