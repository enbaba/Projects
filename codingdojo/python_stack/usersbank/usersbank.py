def__init__(self,name,email):
   self.name = name
   self.email = email
   self.balance = 0
   self.saving = BankAccount("saving", int_rate=0.02, balance=500)
   self.checking = BankAccount("checking", int_rate=0.02, balance=300)

   def make_deposit(self, amount):
       self.balance+= amount
   def make_withdraw(self, amount):
       self.balance -= amount
   def display_user_balance(self):
       print(f"User {self,name}, Balance: {self.balance}")
    

enbaba= User('enbaba', 'enbaba10@gmail.com')