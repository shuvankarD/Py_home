# class person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = person("John", 36)

# p1.name='hui'

# print(p1.name)

class party:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
      print("my name is"+ self.name)
obj = party("kui",90)
obj.myfunc()
