class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.balance = 0

  def deposit(self,amount):
    self.balance += amount
    return self
  def show_balance(self):
    print(f"User {self.name} Your current balance: ${self.balance}")
    return self
  def withdraw(self,amount):
  #check if balance has more the the withdraw amount
    if self.balance>= amount:
      self.balance -= amount
    else:
      self.balance -=10
      print('insuffcient fund')
    return self

#deposit and withdraw account
  '''
  account-balance:1
  deposit(100)deposit(50)deposit(30)withdraw(20).yield_interest()display_account_info()
  deposit(50)deposit(40)withdraw(30)withdraw(10)withdraw(10)withdraw(10).yield_interest()display_account_info()
'''
# create user
enbaba = User('enbaba', 'enbaba10@gmail.com')

print(enbaba.name) # execute name of the user

enbaba.deposit(500).deposit(100).deposit(20).show_balance().withdraw(120).withdraw(100)
enbaba.deposit(600).deposit(200).withdraw(100).withdraw(110).withdraw(120).withdraw(20)

       

