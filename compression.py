# numbers=[1,2,3,4,5]
# odd_numbers=[i for i in numbers if i % 2!=0]
# print(odd_numbers)

# n=[1,2,3,4,5,6,7,8,9] #list compresion
# result=[i if i% 2!=0 else i**2 for i in n]
# print(result)

#dic-compresion
# result={i:"odd" if i % 2!=0 else "even"  for i in n}
# print(result)

# result=(i if i% 2!=0 else i**2 for i in n)
# print(result)
# print(next(result))
# print(tuple(result))

# n=[0,-1,4,0,5,6,-7,-9]
# result=["positive" if i>0  else "Zero" if i==0 else "negative" for i in n]
# print(result)

# s="the quick fox jump fox jump over the lazy dog"

# result=[len(i) for i in s ]
# print(result)



# find the total sum of unique positive even numbers from the given set
numbers = [
    [-1,-2,3,9,1,2],
    [2,3,0,-1,-2,-4],
    [10,9,8,-8,-10,-4],
    [2,3,4,0,-1,-2,-3]
]
even_number=[j for i in numbers for j in i if j % 2==0]
# l_number=[j for j in even_number]
real=(set(even_number))
filter=list(real)
# print(filter)
positive_number=[i for i in filter if i>0]
print(sum(positive_number))