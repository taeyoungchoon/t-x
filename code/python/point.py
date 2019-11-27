class Point:
    def __init__(self, name, x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y

    def hello(self):
        print("hello, ", self.name)

        
dot1 = Point('tom', 1, 2)
dot2 = Point('huck')

dot1.hello()
dot2.x, dot2.y = 10, 10

print('{} at {}, {}'.format(dot1.name, dot1.x, dot1.y))
print('{} at {}, {}'.format(dot2.name, dot2.x, dot2.y))

