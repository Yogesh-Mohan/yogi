class Customer():
    def __init__(self):
        
        self.name = input("Name: ")
        self.mobile = input("Mobile no: ")
        self.email = input("Email id: ")
        self.address = input("Address: ")
    
        
    def display_info(self):
        """Display registered information"""
        print("\n--- Registration Details ---")
        print("Name:", self.name)
        print("Mobile:", self.mobile)
        print("Email:", self.email)
        print("Address:", self.address)
        print("---------------------------")


class Market():
    def __init__(self):
        
        self.name=input("name:")
        self.mobilenumber=int(input("mobile number: "))
        self.address = input("Address: ")
       
       

    def display(self):
        print()

     
        print("name:",self.name)
        print("mobile number:",self.mobilenumber)
        print("Address:", self.address)
        print("-------------------------")
              
        
        
   


registration = Customer()  
registration.display_info()

markets=Market()
markets.display()
