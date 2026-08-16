class PDF:
    def open(self):
        print("Opening PDF")
class Word:
    def open(self):
        print("Opening Word")
class Excel:
    def open(self):
        print("Opening Excel")
files=[PDF(),Word(),Excel()]
for file in files:
    file.open()