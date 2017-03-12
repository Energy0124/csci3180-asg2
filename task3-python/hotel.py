# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : Ling Leong
# Student ID : 1155062557
# Email Addr : alanalan0124@yahoo.com.hk

from room import Room
from attendant import Attendant
from washer import Washer
from refrigerator import Refrigerator
from table import Table
from chair import Chair
from dining_hall import DiningHall


class Hotel:
    def __init__(self):
        pass

    @staticmethod
    def move_room(obj_list, destination):
        for obj in obj_list:
            obj.move_to(destination)


if __name__ == '__main__':
    peter = Attendant("Peter", 58, 10000, 7)
    # stuff in room 2046
    mary = Attendant("Mary", 45, 90000, 1)
    tony = Attendant("Tony", 60, 1000000, 1)
    washer1 = Washer("Washer 1", 55, 1, 5000)
    refrigerator1 = Refrigerator("Refrigerator 1", 50, 1, 5000, 3)
    table1 = Table("Table 1", 20, 1, peter, True)
    chair1 = Chair("Chair 1", 8, 1, peter, False)
    old_room_stuff = [mary, tony, washer1, refrigerator1, table1, chair1]
    # rooms
    old_room = Room("Room 2046", 1)
    new_room = Room("Room 2047", 5)
    dining_hall_1 = DiningHall("Dinning hall 1", 12, 80)
    #  move all the stuff to the new room
    Hotel.move_room(old_room_stuff, new_room)
    # Peter eat something
    peter.move_to(dining_hall_1)
    dining_hall_1.serve_dinner_to(peter)
