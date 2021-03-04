HW1-Recursion for Fibonacci

def Fibonacci(n):
   if n<0:
      return 'Incorrect value'
   elif n==1:
      return 0
   elif n==2:
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2)
n = 7
print(Fibonacci(n))


HW2-Recursion for factorial

def factorial(n):
    if n <= 1:
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print(factorial(n))


HW3-Recursion for digital root

def digital_root(n):
    if n < 10:
        return n
    n=n%10+digital_root(n//10)
    return digital_root(n)
n = 98755433679900987876876
print((digital_root(n)))


HW5-Function to check if a number a Perfect or not

def is_perfect(n):
    perfect_sum = 0
    for i in range(1, n):
        if n % i == 0:
           perfect_sum += i
    return perfect_sum == n
number = int(input('Enter number: '))
if is_perfect(number):
    print("%d is PERFECT" % (number))
else:
    print("%d is NOT PERFECT" % (number))


HW6-Amicable numbers from slides

x = 220
y= 284
sum1=0
sum2=0
for i in range(1,x):
    if x%i == 0:
        sum1 += i
for j in range(1,y):
    if y%j == 0:
        sum2 += j
if sum1==y and sum2==x:
    print('Amicable!')
else:
    print('Not Amicable!')
