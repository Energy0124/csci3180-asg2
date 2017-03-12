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

from fixture import Fixture


class DumbFixture(Fixture):
    def __init__(self, name, weight, position, person_in_charge):
        Fixture.__init__(self, name, weight, position)
        self._person_in_charge = person_in_charge

    @property
    def person_in_charge(self):
        return self._person_in_charge

    def assign_to(self, person_in_charge):
        self._person_in_charge = person_in_charge

    def move_to(self, destination):
        self._person_in_charge.carry_to(self, destination)
