#Q1: Nearest leap year in the increasing side
# Function to check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Input a year
year = int(input("Enter a year: "))

# Find the next leap year
while not is_leap_year(year):
    year += 1

print("Nearest leap year:", year)

# perfect number or not---6-->1,2,3=6

def is_perfect_number(n):
    if n <= 1:
        return False

    divisors_sum = 0
    for i in range(1, n // 2 + 1): 
        if n % i == 0: 
            divisors_sum += i
    return divisors_sum == n

number = int(input("Enter a number: "))
if is_perfect_number(number):
    print(number," is a perfect number.")
else:
    print(number," is not a perfect number.")

# armstrong number in a given range
#Q3: Find all armstrong number in a given range (100 to 1000)
#153 => 125 + 27 + 1 => 153
low=int(input("Enter the 1st number :"))
upp=int(input("Enter the 2nd number :"))

for i in range(low, upp + 1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if i == sum:
        print(i)
        
        #------------ Feb--15-----------
        
#Q)Searching for an element in a list?
def search_num(list,search_element):
    for i in list:
        if search_element == i:
            return True
    return False
list1=[]
element=1
if (search_num(list1,element)):
    print("found")
else:
    print("not found")
    
#Q) Finding duplicates in list using empty set    
def duplicates(list):
    unique=[]
    duplicate=[]
    for i in list:
        if i in unique:
            duplicate.append(i)
        else:
            unique.append(i)
    print(unique)
    print(duplicate)
duplicates([1,2,3,4,5,1,2])

#Q) Finding duplicates in list using empty sets for time complexity o(1)
def duplicates(list):
    unique=set()
    duplicate=set()
    for i in list:
        if i in unique:
            duplicate.append(i)
        else:
            unique.append(i)
    print(unique)
    print(duplicate)
duplicates([1,2,3,4,5,1,2])  