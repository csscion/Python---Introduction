def display_list(my_list):
    print(my_list)

def user_choice():
    choice="wrong"
    
    while True:
        choice = input("Please enter input)")
        
        
        if choice.isdigit():
            choice = int(choice)

            if 0 <= choice <= 2:
                print("Valid input",choice,"of ",type(choice))
                return choice
            else:
                print("incorrect range-entered input is==",choice,type(choice))
                
        else:
            print("non digit choice-Please enter a numeric value.")
    
            


            

my_list=[0,1,2,3,4,5,6,7,8,9,10]
display_list(my_list)
result =user_choice()
print("result is",result,type(result))


