print("Enter your weight")
m=float(input())
print("Enter your height")
H=float(input())
BMI=m/H**2
if (BMI<=0):
    print("Input is invalid try again you bitch")
else:
    print("Your BMI ratio is",BMI)


