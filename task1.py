#Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n<2:
        return 1
    else:
        return n* (factorial(n-1))  #3*2*1*0

a=int(input("enter a number:"))

result=factorial(a)
print(f'factoral of {a} is {result}')