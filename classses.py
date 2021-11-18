class Cookie:
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    

cookie_one = Cookie('red')
cookie_two = Cookie('blue')

print(cookie_one.get_color())
print(cookie_two.get_color())

cookie_one.set_color('purple')

print(cookie_one.get_color())