class Education:
    def ug(self):
        print("under graduate course:")

    def pg(self):
        print("Post graduate course")

class Arts(Education):
    def bsc(self):
        print("Bsc")

    def bed(self):
        print("BEd..")

    def ba(self):
        print("BA")

    def bba(self):
        print("bba")

class Engineering(Education):

    def be(self):
        print("be")

    def bTech(self):
        print("btech")

class Medicine(Education):

    def physiyo(self):
        print("physiyo")

    def dental(self):
        print("Dental")

    def mbbs(self):
        print("Mbbs")

print("Hierarical inheritane: ")
a=Arts()
a.ug()
a.ba()
a.bba()
a.bed()
a.bsc()
a.pg()

e=Engineering()
e.ug()
e.be()
e.bTech()

m=Medicine()
m.ug()
m.mbbs()
m.dental()
m.physiyo()
m.pg()