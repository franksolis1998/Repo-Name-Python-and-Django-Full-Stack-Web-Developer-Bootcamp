# class Animal():

#     def __init__(self):
#         print("ANIMAL CREATED")

#     def whoAmI(self):
#         print("ANIMAL")

#     def eat(self):
#         print("EATING")

# class Dog(Animal):

#     def __init__(self):
#         # Animal.__init__(self)
#         print("DOG CREATED")

#     def bark(self):
#         print("WOOF")

#     def eat(self):
#         print("DOG EATING")



# mydog = Animal()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()




class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}. Author: {}, Pages: {}".format(self.title,self.author,self.pages)


    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is deleted")

b = Book("Python", "Frank", 200)
print(len(b))
mylist = [1,2,3]
print(mylist)