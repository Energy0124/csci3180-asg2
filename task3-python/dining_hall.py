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


class DiningHall(Room):
    def __init__(self, name, postion, dinner_price):
        Room.__init__(self, name, postion)
        self._dinner_price = dinner_price

    @property
    def dinner_price(self):
        return self._dinner_price

    def serve_dinner_to(self, obj):
        if obj.position == self.position:
            if obj.pay(self._dinner_price) > 0:
                print obj.name + " finished the dinner."
            else:
                print obj.name + " didn't have enough money."
        else:
            print obj.name + " was too far away to be served."
