# x = 25

# def my_function():
#     x = 50
#     return X

# # print(x)
# # print(my_function)
# my_function()
# print(x)





# name = 'This is a global name!'

# def greet():

#     def hello():
#         print("hello"+name)

#     hello()

# greet()
# print(name)



x = 50

def func():
    # global x
    x = 1000 
    return x

print("before funcion call, x is:",x)
x = func()
print("after function call, x is: ",x)