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

from smart_fixture import SmartFixture


class Refrigerator(SmartFixture):
    def __init__(self, name, weight, position, battery_capacity, initial_temperature):
        SmartFixture.__init__(self, name, weight, position, battery_capacity)
        self._temperature = initial_temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self._temperature = new_temperature
        print self.name + " was set to " + "%.1f" % new_temperature + " degrees Celsius."
