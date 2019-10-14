class family_member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age = int(self.age + 1)


class kids(family_member):

    bed_time = 8
    num_kids = 0

    def __init__(self, name, age, bed_time=None):
        family_member.__init__(self, name, age)
        if bed_time is None:
            self.bed_time = kids.bed_time
        else:
            self.bed_time = bed_time
        num_kids = +1

    def print_bedtime(self):
        print("{}'s bedtime: {}".format(self.name, self.bed_time))

    @classmethod
    def change_bed_time(cls, new_time):
        cls.bed_time = new_time


Isla = kids("Isla", 3)

Adrian = kids("Adrian", 10, 9)


Isla.print_bedtime()
Adrian.print_bedtime()
kids.change_bed_time(10)
Isla.print_bedtime()
Adrian.print_bedtime()

