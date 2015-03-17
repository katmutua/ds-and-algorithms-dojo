class Sets:

    def __init__(self):
        self.set_a = {2, 4, 5, 5, 6}
        self.set_b = {2, 4}

    def operations(self):
        print self.set_a | self.set_b
        print self.set_a.union(self.set_b)
        print self.set_a & self.set_b
        print len(self.set_b)
        print self.set_a.intersection(self.set_b)
        self.set_a.difference(self.set_b)
        print self.set_a
        self.set_a.add(5)
        print self.set_a

        self.set_b.remove(4)
        print self.set_b


basic_structures = Sets()
basic_structures.operations()

class Lists:
    def __init__(self, list):
        self.simple_list = list

    def list_operations(self):
        addition = int(input("Please enter a number\n"))
        if not isinstance(addition, int):
            raise TypeError('oops why add a string to a list bruh?')
        else:
            self.simple_list.append(addition)
        print ''.join(str(self.simple_list)).strip('[]')


simple_list = Lists([2, 5,6,7,8,8])
simple_list.list_operations()


class StringManipulation:

    def __init__(self):
        self.simple_string = 'amalgamation'

    def operations(self):
        print self.simple_string.upper()
        print self.simple_string.split('gama')
        print self.simple_string.count('a')


stringer = StringManipulation()
stringer.operations()


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)


class Reversal:

    def __init__(self, sample_string):
        self.sample_string = sample_string

    def reverse_string(self):
        string_list = list(self.sample_string)
        string_list.reverse()
        print ''.join(string_list)


string_reversal = Reversal('insertionsortamalgamation')
string_reversal.reverse_string()
