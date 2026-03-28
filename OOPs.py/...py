class Test:
    count = 0

    def __init__(self, x):
        self.x = x
        Test.count += x

    @classmethod
    def show(cls):
        print(cls.count)

t1 = Test(2) #x assumed as 2 (test.count +=x = +2)
t2= Test(3) #x assumed as 3 (2 + +=3 = 5)
t3 = Test(5) #x assumed as 5 (5 + +=5 = 10)

t1.show()