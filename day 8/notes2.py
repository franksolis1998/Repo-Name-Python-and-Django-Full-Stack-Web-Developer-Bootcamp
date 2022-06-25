# if 1 == 1:
#     if 1 < 2:
#         print('hello')
#     elif 3 == 3:
#         print('elif ran')
#     else:
#         print('last')

# for loops

# seq = [1,2,3,4,5,6]

# for jelly in seq:
#     #Code here
#     print(jelly)

# d = {"Sam":1, "Frank":2, "Dan":3}

# for k in d:
#     print(k)
#     print(d[k])



# mypair = [(1,2),(3,4),(5,6)]

# for (tup1,tup2) in mypair:
#     print(tup2)
#     print(tup1)

# i = 1 
# while i<5:
#     print("i is:{}".format(i))
#     i = i + 1

# x = [1,2,3,4]

# out =[]
# for num in x:
#     out.append(num**2)

x = [1,2,3,4]

out =[num**2 for num in x]
print(out)