

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average(num_list))
    print(find_min_max(num_list))

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    
def get_user_input():
    userinput=input()
    postsplit=userinput.split(",")
    i=0
    while i!=len(postsplit):
        postsplit[i]=float(postsplit[i])
        i+=1
    return postsplit


def calc_average(input):
    print("calc_average")
    sum=0
    for item in input:
        sum += item
    return sum/len(input)


def find_min_max(input):
    min=input[0]
    max=input[0]
    for item in input:
        if item<min:
            min=item
        if item>max:
            max=item
    return [min, max]
    

def sort_temperature(input):
    return 

def calc_median_temperature(input):
    return

if __name__ == "__main__":
    main()
          
