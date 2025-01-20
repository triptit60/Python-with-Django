#Map(with lambda function)=function kam garxa
#filter ma filtered value return matra garne kam garxa
#reduce(from funtiontools import reduce)
# def cube(x):
#     return x**3

# no=[1,2,3,4,5,6,7,8,9,10]

# cube_numbers=map(cube,no)
# print(list(cube_numbers))

# no=[2,3,4,5,6,7,8,9]
# filterred_no=filter(lambda x: x%2!=0,no)
# print(list(filterred_no))
from functools import reduce
no=[3,4,6,2,4]
reduced_no=reduce(lambda x,y:x*y,no)
print(reduced_no)



#database=query,sql database-xampp
#database query