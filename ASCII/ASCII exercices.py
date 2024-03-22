import listmaker

tempnum = input("Enter a bunch of numbers: ")
nums = []
nums = listmaker.create(tempnum, nums)
nums = listmaker.listint(nums)


num1 = int(input("Enter a number: "))
num2 = int(input("\nEnter a number: "))
bla = input("\nEnter a word: ")
palin = input("\nEnter a word to check if it is a palindrome: ")




def numadd(x,y):
    ans = x + y
    return ans

print(numadd(num1,num2))

def un(x):
    return 'un' + x

print(un(bla))


def palindrome(x):
    x = x.lower()
    if x == x[::-1]:
        return f"{x} is a palindrome"
    else:
        return f"{x} is not a palindrome"

print(palindrome(palin))


def oddeven(x):
    odd = []
    even = []
    tOdd = 0
    tEven = 0
    
    for i in range(0,len(x)):
        if (x[i] % 2) != 0:
            odd.append(x[i])
            tOdd += x[i]
        else:
            even.append(x[i])
            tEven += x[i]
            
    nOdd = len(odd)
    nEven = len(even)
    avOdd = tOdd /  nOdd
    avEven = tEven / nEven
    return f"Odd numbers = {odd}\nEven numbers = {even}\nNumber of odd numbers = {nOdd}\nNumber of even numbers = {nEven}\nTotal of odd numbers = {tOdd}\nTotal of even numbers = {tEven}\nAverage of odd numbers = {avOdd}\nAverage of Even numbers = {avEven}"
        
print(oddeven(nums))