class Circle:
    def __init__(self,radius,color):
        if not isinstance(radius,(int,float)):
            raise Exception('Please input a positive integer')
        else:
            self.radius = radius
            
        if not isinstance(color,str):
            raise Exception('Invalid input. Please try again. Input a string')
        else:
            self.color = color
    def __str__(self):
        return ' {} circle withradius {}'.format(self.color,self.radius)
    def get_area(self):
        return self.radius**2*3.14
    def circumference(self):
        return 2*self.radius*3.14
    def __add__(self,other):
        return Circle(self.radius+other.radius,self.color)
   

class Person:
    def __init__(self,name,last_name,age,gender,student,password): 
        assert isinstance(name,str),'Please input a string for name'
        assert isinstance(last_name,str),'Please input a string for lastname'
        assert isinstance(age,int),'Please input a positive integer for age'
        assert isinstance(gender,str),'Please input a string for gender'
        assert isinstance(student,bool),'Student attribute takes values True or False'
        self.name=name 
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.__password = password
    def Greeting(self,second_person):
        return 'Welcome dear {}'.format(second_person.name)
    
    def Goodbye(self):
        print( "Bye everyone!" )
    
    def Favourite_num(self, num1):
        return 'My favorite number is {}'.format(num1)
    def read_file(self,filename):
        try:
            f = open('{}.txt'.format(filename))
        except FileNotFoundError:
            print ("No such file or directory.")
            
            
class RomanNumber:
    def __init__(self, roman_number):
        self.number = roman_number
        assert self.convert_to_roman(self.convert_to_num()) == roman_number,'Not Valid Roman Number'
    def get_num(self):
        return self.number
    
    def set_num(self, num1):
        self.number = num1

    def convert_to_num(self):
        num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for key,value in enumerate(self.number):
            if (key+1) == len(self.number) or num_dict[value] >= num_dict[self.number[key+1]]:
                result += num_dict[value]
            else:
                result -= num_dict[value]
        return result
    
    def convert_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    
    def __add__(self, x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num()+x.convert_to_num()))
    def __sub__(self, x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num()-x.convert_to_num()))
    def __mul__(self, x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num()*x.convert_to_num()))
    def __pow__(self,x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num()**x.convert_to_num()))
    
    
class Polygon:
    def __init__(self, n_of_sides):
        assert isinstance(n_of_sides,int),"Please input a positive integer"
        assert n_of_sides>=3, 'import existing polygon'
        self.n = n_of_sides
        self.sides = list()

    def input_sides(self, sides):
        assert isinstance(sides,list),"sides must be given as list"
        self.sides = sides
        assert len(sides)==self.n,'length of list not equal length of sides '

    def disp_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
    def get_perimeter(self):
        return sum(self.sides)

class Quadrilatera(Polygon):
    def __init__(self):
        super().__init__(4)
class  Rectangle(Quadrilatera): 
    def input_sides(self,s):
        super().input_sides(s*2)
    def get_area(self):
        return self.sides[0]*self.sides[1]
class  Square(Rectangle):
    def input_sides(self,s):
        super().input_sides(s*2)
    
        