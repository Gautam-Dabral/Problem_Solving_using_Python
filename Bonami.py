import math

# decorator

# def speedTest():
#     def wrapper(*args, **kwargs):
#         startTime = time()
#         res = f(*args, **kwargs)
#         endTime = time()
#         print(f"time taken {endTime - startTime} seconds")
#         return res
#     return wrapper

# def perfect(n) :
#     factors = [x for x in range(1, n//2+1) if n%x==0]
#     print(factors)
#     return n == sum(factors)

# print(perfect(6))

################################################################

# def sublist(l1, l2) :
#     if l1 == []: return True
#     else:
#         for i in range(len(l2)):
#             if l1[0] == l2[i]:
#                 pos = i
#                 for j in range(len(l1)):
#                     if pos<len(l2) and l1[j] == l2[pos] :
#                         pos += 1
#                     else :
#                         break
#                 else:
#                     return True
#         return False
                    
# print(sublist([2,3,5], [1,2,3,4,5]))      # => False

################################################################

# def printThirdLinesOnly ():
#     listOfLines = []
#     line = input()
#     while line:
#         listOfLines.append(line)
#         line = input()

#     i = 2
#     while i < len(listOfLines):
#         print(listOfLines[i])
#         i += 3

# printThirdLinesOnly()

################################################################

# def countRepeated(l):
#     repeatCount = 0
#     while l:
#         toCheck = l[0]
#         if toCheck in l[1:]:
#             repeatCount += 1
#         while toCheck in l:
#             l.remove(toCheck)
#     return repeatCount

# print(countRepeated([1,2,2,3,4,2,3])) # => 2

# Alternative solution using dictionary (frequency table)

# def countRepeated (l):
  
#   in_dict , counter = {} , 0
  
#   for items in l:
#     if items not in in_dict.keys():
#       in_dict[items] = 1
#     else :
#       in_dict[items] += 1

#   for keys in in_dict:
#     if in_dict[keys] > 1:
#       counter += 1
#   return counter

################################################################
# def sumOfThreeCubes(n):
#     last = math.ceil(math.pow(n, 1/3))

#     for i in range(1,last):
#         for j in range(1,last):
#             for k in range(1,last):
#                 if math.pow(i,3) + math.pow(j, 3) + math.pow(k, 3) == n:
#                     return (i,j,k)
#                 elif math.pow(i,3) + math.pow(j, 3) + math.pow(k, 3) > n:
#                     return False


# print(sumOfThreeCubes(11))

