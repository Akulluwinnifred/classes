#define five classes with atleast shish method taking atleast five parameters and create atleast three objects

class Phone:
    def __init__(self, name,color,storage,ram,price):
        self.name = name
        self.color = color
        self.storage = storage
        self.ram = ram
        self.price = price

phone1 = Phone("itel","black","32gb","4gb",400000)


phone2 = Phone("tecno","blue","64gb","8gb",800000)


phone3 = Phone("samsung","choco","128gb","16gb",12000000)




class Animal:
    def __init__(self,color,size,name,gender,age):
        self.color = color
        self.size = size
        self.name = name
        self.gender = gender
        self.age = age

lion = Animal("yellow","big","Simba", "male",5)


tiger = Animal("white","medium","Tigger", "female",7)


dog = Animal("brown","small","Rex", "male",3)

   



class  Forest:
    def __init__(self,name,location,size,ftype,tree_height):
        self.name = name
        self.location = location
        self.size = size
        self.ftype = ftype 
        self.tree_height = tree_height



forest1 = Forest("Mabira","Jinja","large","Temperate","15ft")

forest2 = Forest("Maramagambo","Eastern","medium","Tropical","40ft")

forest3 = Forest("Bwindi","western","small","Temperate","30ft")





class Lake:
      def __init__(self,name,location,depth,width,ltype):
          self.name = name
          self.location = location
          self.depth = depth
          self.width = width
          self.ltype = ltype

lake1 = Lake("L.turkana","kenya","60ft","50km","salty")

lake2 = Lake("L.kwania","Northern","80ft","100km","faulting")

lake1 = Lake("L.victoria","central","100ft","400km","downwarping")





class Movie:
    def  __init__(self,title,director,price,rating,duration):
        self.title= title
        self.director = director
        self.price = (price)
        self.rating = (rating)
        self.duration = duration


movie1 = Movie("inception","Christopher","30000shillings","5-star","120mins")

movie2 = Movie("Premonition","Adakirikiri","50000shillings","4-star","200mins")

movie3 = Movie("Better_half","Kadiri","80000shillings","5-star","300mins")








