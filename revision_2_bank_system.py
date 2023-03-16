'''
Bank System : 
    - create new account [name , gender , age]
    - deposit 
    - withdraw 
    - view balance 
   
'''  

class User : 
    def __init__ (self,name,gender,age):
        print (f"welcome {name}")
        self.name = name 
        self.gender = gender 
        self.age = age 
        

    def show_details (self) : 
        print ('personal Information .. ')
        print (f"name {self.name}")
        print (f"gender {self.gender}")
        print (f"age {self.age}")
        print (f"balance {self.balance}")

    
class Bank (User) :
    def __init__ (self,name,gender,age):
        super().__init__ (name,gender,age)
        self.balance = 0

    def deposit (self,amount) : 
        self.balance += amount 
        print (f"your currently balance = {self.balance}") 

    def withdraw (self,amount) : 
        if amount < self.balance : 
            self.balance -= amount 
            print (f"withdraw succeed .. your currently balance = {self.balance}") 

        else : 
            print (f"you don't have sufficient credit , your currently balance {self.balance}")


user_1 = Bank ('mohamed','mail',30) 

user_1.show_details ()

user_1.deposit(100)
user_1.deposit(200)

user_1.withdraw(1500)