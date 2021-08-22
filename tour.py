class main_info:
    
    def place(self):
        pass
    
    def Transport(self):
        pass
    
    def first_day(self):
        pass
    
    def secound_day(self):
        pass
    
    def third_day(self):
        pass
    
    def fourth_day(self):
        pass
    
    def price(self):
        pass
    
    def info(self):
        self.place()
        self.Transport()
        self.first_day()
        self.secound_day()
        self.third_day()
        self.fourth_day()
        self.price()
class sylhet(main_info):
    def place(self):
        print("Place ==> [Jaflong] => [Bisnakandi] => [Sathchori National Forest]=>[BHOLAGONJ]=>[Rema Kalenga Reserve Forest]")
    def Transport(self):
        print("Transport ==> BUS")
    def first_day(self):
        print(" 1st Day => Tourist visit Jaflong ==> Tourist visit Bisnakandi")
    
    def secound_day(self):
        print(" 2nd Day => Tourist visit Sathchori National Forest ")
    def third_day(self):
        print(" 3rd Day => Tourist visit BHOLAGONJ ")
    def fourth_day(self):
        print(" 4th Day => Tourist visit Rema Kalenga Reserve Forest ")
    def price(self):
        print("packeg cost ==> 10000tk ")
        print("******************************************END****************************************************")
        print(" ")
class Sundarban(main_info):
    def place(self):
        print("Place ==> [Kotka Beach] => [Karmajal] => [Hiron Point]=>[Dublar CharIsland]=>[Tin Kona Island]")
    def Transport(self):
        print("Transport ==> BUS")
    def first_day(self):
        print(" 1st Day => Tourist visit Kotka Beach")
    def secound_day(self):
        print(" 2nd Day => Tourist visit Karmajal ==> Tourist visit Hiron Point ")
    def third_day(self):
        print(" 3rd Day => Tourist visit Dublar Char Island ")
    def fourth_day(self):
        print(" 4th Day => Tourist visit Tin Kona Island ")
    def price(self):
        print("packeg cost ==> 8000tk ")
        print("*******************************************END************************************************")
        print(" ")
class Cox_bazar(main_info):
    
    def place(self):
        print("Place ==> [Inani Beach] => [Cox's Bazar Beach] => [Marine Drive]=>[Himchori]")
    def Transport(self):
        print("Transport ==> Air")
    def first_day(self):
        print(" 1st Day => Tourist visit Cox's Bazar Beach")
    def secound_day(self):
        print(" 2nd Day => Tourist visit Inani Beach ")
    def third_day(self):
        print(" 3rd Day => Tourist visit Marine Drive ")
    def fourth_day(self):
        print(" 4th Day => Tourist visit Himchori ")
    def price(self):
        print("packeg cost ==> 15000tk ")
        print("*******************************************END************************************************")
object=sylhet()
object.info()
object=Sundarban()
object.info()
object=Cox_bazar()
object.info()
    
