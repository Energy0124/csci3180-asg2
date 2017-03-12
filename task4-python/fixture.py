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

class Fixture:
    def __init__(self, name, weight, position):
        self._name = name
        self._weight = weight
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position
