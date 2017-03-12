from smart_fixture import SmartFixture


class Washer(SmartFixture):
    def wash(self):
        print self.name + " finished a wash procedure."
