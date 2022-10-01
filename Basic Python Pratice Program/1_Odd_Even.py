class odd_even:
    def __init__(self,number):
        self.number=number

    def predict(self):
        if(number%2==0):
            return 1
        else:
            return 0

number=int(input("Enter any number"))
obj=odd_even(number)
if(obj.predict()==1):
    print(str(number) +" is a even number")
else:
    print(str(number) + " is a odd number")
