# Melody Gatan, Kenton La
# 10/17/2023
# A game where a player has to open 3 doors to win

from basic_door import BasicDoor
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from random import choice
from check_input import get_int_range


def open_door(door):
    print(door.examine_door())
    while door.is_unlocked() == False:
        input = get_int_range(door.menu_options(), 1, door.get_menu_max())
        door.attempt(input)
        if door.is_unlocked() == False:
            print(door.clue())
        else:
            break
    print(door.success())


def main():
    count = 0
    print('Welcome to the Escape Room. You must unlock 3 doors to escape...\n')

    while count < 3:
        doors = [
            ComboDoor(),
            BasicDoor(),
            DeadboltDoor(),

        ]
        door = choice([door for door in doors])
        open_door(door)
        count += 1
    print('Congratulations! You escaped...this time.')


main()
