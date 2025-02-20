
# --------------------------fibnocci series in pattern-------------------------------    
# def fib(n):
#     a=0
#     b=1  
#     fib=[]
#     if n<0:
#         print("invalid")
#     elif(n==1):
#         return b
#     else:
#       for _ in range(0,n):
#           fib.append(a)
#         #   c=a+b
#         #   a=b
#         #   b=c
#         #method 2 tuple unpacking
#           a,b=b,a+b
#       return fib   

# def pattern(n):
#     list=fib(n)
#     for i in range(n):
#         for j in range(n-1-i):
#             print(list[j],end="")
#         print()
            
# pattern(5)  

# --------------Traingle fib_ pattern------------

# def fib_pattern(n):
#     a=0
#     b=1
#     for i in range(n):
#         for j in range(n-i-1):
#             print(a,"  ",end="")
#             a,b=b,a+b
#         print()          
# fib_pattern(5)


# ------------- Rotate an Array by K Elements----------
# def rotate_array(arr, k):
#     k = k % len(arr) #for getting back to original if k greater then len of array
#     return arr[-k:] + arr[:-k]
# array=[1,2,3,4,5]
# print(rotate_array(array,2))

#-----------primenumber---------
# def is_prime(num):
#     if num<=1:
#         return False
#     else:
#         for i in range(2,int(num**0.5)+1):  #for i in range(2,num//2+1):
#             if i%2==0:
#                 return False
#         return True
# def print_prime(n):
#     for i in range(1,n+1):
#         if  is_prime(i):
#             print(i)
# print_prime(3) 


# str1="ramesh"
# r=sorted(str1)
# print(str1)
