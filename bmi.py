





def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/(height**2)
    if bmi>25.0:
        print(bmi)
        print("overweight")
    elif bmi>=18.5:
        print(bmi)
        print("Normal weight")
    else: 
        print(bmi)
        print("underweight")

calculate_bmi(weight=73, height=20)