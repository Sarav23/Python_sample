class Education():
    def ug(self):
        print("Under Graduate courses:")


    def pg(self):
        print("post graduate course")


class Arts(Education):
    def bsc(self):
        print("Bsc")

    def bed(self):
        print("BEd..")

    def ba(self):
        print("BA")

    def bba(self):
        print("bba")

    def ug(self):
        print("Under graduate courses and diplomo courses")

    def pg(self):
        print("Post graduate courses and Engineering courses")

e=Arts()
e.pg()
e.ug()
e.bsc()
e.ba()
e.bed()
e.bba()