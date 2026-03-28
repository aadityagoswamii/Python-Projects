
class Demo:
    okado = 10

    def __init__(self, okado):
        self.okado = okado

    def show_instance(self):
        print(self.okado)

d1 = Demo(50)
d2 = Demo(100)

d1.show_instance()  # 50
d2.show_instance()  # 100


