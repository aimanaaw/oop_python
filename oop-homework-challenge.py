class Account():
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
    print(f"Class created. {self.owner} has {self.balance}")

  def owner_balance(self):
    print(f"{self.owner}'s balance is {self.balance}")

  def deposit(self, add_amount):
    self.balance = self.balance + add_amount
    print (f"{add_amount} has been added. The new balance is {self.balance}")
    return self.balance

  def withdraw(self, remove_amount):
    if self.balance < remove_amount: 
      print (f"insufficient balance to withdraw")
    else:
      self.balance = self.balance - remove_amount
      print (f"{remove_amount} has been withdrawn. The new balance is {self.balance}")
      return self.balance
  
  def __str__(self):
    return f"Account owner: {self.owner}. Account balance: {self.balance}"


jose = Account('jose', 1000)
jose.owner_balance()
jose.deposit(600)
jose.withdraw(200)
print(jose)
