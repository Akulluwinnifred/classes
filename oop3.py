class Lake:
      def __init__(self,name,location,depth,width,size,ltype):
            self.name = name
            self.location = location
            self.depth = depth
            self.width = width
            self.size = size
            self.type = ltype
#shish method(__init__) is a special method we use in python to identify properties of a class
#the first parameter in the shish parenthesis() refers to an individual property of a class and not an attribute

#creating objects of a class Lake
            lake1=Lake("victoria", "central", "1200ft", "400m", "500km^3", "salty")






class River:
      def __init__(self,a, b, c):
            self.name= a
            self.location= b
            self.length= c
#any method of a class must have a parameter "self"
river1 = River("R.Nile", "Central", "600km")

#creating an object of a class is called instanciating
#the shish function is called a constructor and is used to initialize an instanciated object
#it is used to give value to an instanciated object