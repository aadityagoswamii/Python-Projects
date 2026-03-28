class Sounter: #inside the class we can use any word but first letter Capital only!
    jameel = 0

    def __init__(self):
        Sounter.jameel += 1

    @classmethod
    def aslam(cls):  #method(function inside class)
        print(cls.jameel) #cls = represents class itself inside a class method

c = Sounter()
c = Sounter()
c = Sounter()  #the# class is independent identity so it will count objects overall not individually(total 6)
c = Sounter()  #this will happen only in the presence of @classmethod
c = Sounter()
c = Sounter()
c = Sounter()
c = Sounter()
c = Sounter()
c = Sounter()


c.aslam()
Sounter.aslam()