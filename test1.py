#test

class Calculator :

    def __init__( self, first, second) :
        self.first = first
        self.second = second

    def setdata(self, first, second) :
        self.first = first
        self.second = second
    
    def add ( self ) :
        result = self.first + self.second
        return result
    
    def sub (self) :
        result = self.first - self.second
        return result

    def div ( self ) :
        result = self.first / self.second

        return result

    def mul ( self) :
        result = self.first * self.second
        return result


a = Calculator( 8, 1.5) 

result = a.add()

print ( result )

print ( a.mul())

print ( a.sub())
print ( a.div())




