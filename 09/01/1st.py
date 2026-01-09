def oddeven():
    
    num = int(input("Enter a number"))
    if(num % 2 == 0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")    
        
def oddOrEvenRange():
    lower =int(input("Enter a lower number"))
    upper =int(input("Enter a upper number"))         

    for num in range(lower, upper+1):
        if(num % 2 == 0):
            print(f"{num} is even")
        else:
            print(f"{num} is odd") 
def main():
    # oddeven() 
    oddOrEvenRange()  
    
if __name__ == "__main__":
    main()        

