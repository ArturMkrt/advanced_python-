class RomanNumeral:
    def __init__(self,num): 
        self.num = num
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        self.roman_num = ''
        i = 0
        while  num > 0:
            for _ in range( num // val[i]):   
                self.roman_num += syb[i]
                num -= val[i]            
            i += 1
    def __add__(self,other):
        obj = RomanNumeral(self.num + other.num)
        return obj
    def __mul__(self, other):
        obj = RomanNumeral(self.num * other.num)
        return obj
    def __sub__(self,other):
        obj = RomanNumeral(self.num - other.num)
        return obj
    def to_decimal(self):
        return self.num
    def __str__(self):
        return self.roman_num
    
class Person:
    def __init__(self,name,last_name,age,gender,student,password): 
        self.name=name 
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.__password = password
        if isinstance(student,bool):
            self.student=student
        else:    
            raise Exception("Student attribute takes values True or False")
    def Greeting(self,second_person):
        return 'Welcome dear {}'.format(second_person.name)
    def Goodbye(self):
        return "Bye everyone!"
    def Favourite_num(self, num1):
        return 'My favorite number is {}'.format(num1)
    
    
class Polygon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides = list()

    def input_sides(self, sides):
        self.sides = sides
        print(self.sides)

    def disp_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
    def get_perimeter(self):
        return sum(self.sides)

class Quadrilatera(Polygon):
    def __init__(self):
        super().__init__(4)
class  Rectangle(Quadrilatera):
    def __init__(self):
        super().__init__()   
    def input_sides(self,s):
        super().input_sides(s*2)
    def get_area(self):
        return self.sides[0]*self.sides[1]
class  Square(Rectangle):
    def __init__(self):
        super().__init__()
    def input_sides(self,s):
        super().input_sides(s*2)