def oddeven():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")    

def oddOrEvenRange():
    lower = int(input("Enter lower number: "))
    upper = int(input("Enter upper number: "))         

    for num in range(lower, upper + 1):
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd") 

def reversal():
    num = int(input("Enter a number: "))
    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    print(f"{original_num} reversed is {reversed_num}")
    
def factorial(num):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(num-1)
    
def main():
    # oddeven()
    # oddOrEvenRange()
    reversal()
    factorial()

if __name__ == "__main__":
    main()
