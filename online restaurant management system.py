#restorant management system

total_bill=0
print("=======Welcome Sir/Mam to our Restaurant========")


def show_menu():
    print("---------------------------")
    print("     1,Pizza-₹180")
    print("     2,Burger-₹120")
    print("     3,Pasta-₹90")
    print("     4,Chowmine-80")
    print("     5,Coffee-₹70")
    print("     6,Tea-₹20")
    print("     7,Cold drink",80)
    
def take_order():
    global total_bill
    Order=int(input("Please give your order(1-8):"))
    match Order:
        case 1:
            qty=int(input("Enter Pizza quantity:"))
            total_bill+=180*qty
        case 2:
            qty=int(input("Enter Burger quantity:"))
            total_bill+=120*qty
        case 3:
            qty=int(input("Enter Pasta quantity:"))
            total_bill+=90*qty
        case 4:
            qty=int(input("Enter Chowmine quantity:"))
            total_bill+=80*qty
        case 5:
            qty=int(input("Enter Cup of Coffee:"))
            total_bill+=70*qty
        case 6:
            qty=int(input("Enter Cup of Tea:"))
            total_bill+=20*qty
        case 7:
            qty=int(input("Enter glass of cold drink:"))
            total_bill+=80*qty
     
        case _:
            print("Invalid item")
        
    
    

    
def Show_bill():
    print("\n========Bill===========") 
    print("Total Bill",total_bill)
     

def main():
    condition=True
    while condition:
        #show_menu()
        print("_______Choice you want___________")
        print("     1.Show Menu")
        print("     2. Order Food")
        print("     3.Show Bill")
        print("     4.Exit")
        choice=int(input("enter youe Choice(1-4): "))

        match choice:
            case 1:
                show_menu()
            case 2:
                take_order()
            case 3:
                Show_bill()
                
            case 4:
            	condition=False
            case _:
                  print("Invalid choice")
                  
print("\n======Restaurant Management system=======")
main()
print ("THANKS FOR VISITING US😊😊")