balance = 0

def deposite(x):
  global balance
  balance += x
  print(f"{x} deposited, your new balance is {balance}")
  print(f"local balance is {balance}")

def withdraw(x):
  global balance
  balance -= x
  print(f"{x} withdrawn, your new balance is {balance}")  

deposite(10000)
withdraw(1000)

deposite(100)
withdraw(7000)