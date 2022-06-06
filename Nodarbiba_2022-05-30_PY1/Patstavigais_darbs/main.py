import random

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

class Account:

    def __init__(self):
        self.number = random_with_N_digits(21)
        self.balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.balance =+ amount
            return print("Added: ",amount)
        else:
            print("Negative numbers not allowed!")    
        
    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance = (self.balance - amount)
            return print("Withdrawn: ",amount)
        else:
            print("Illgal operation!")

class Client:

    def __init__(self, client_name):
        self.client_name = client_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        total_amount = []
        for account in self.accounts:
            total_amount.append(account.balance)
        return sum(total_amount)
    

class Bank():

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.clients = []

    def add_client(self, client_name):
        self.clients.append(client_name)

    def get_total_deposits(self):
        ############################
        #nepaspeju realizēt, uz ātro neatradu kā strādāt ar datiem starp klasem, brīvā brīdī turpināšu
        ############################
        pass


banka = Bank(bank_name="Jaunā Banka")

aldis = Client(client_name="Aldis")
zane = Client(client_name="Zane")

banka.add_client(aldis)
banka.add_client(zane)

account_1 = Account()
print(account_1.number)
aldis.add_account(account_1)

account_1.add_money(600)
account_1.withdraw(30)
print(account_1.balance)


account_2 = Account()
aldis.add_account(account_2)
account_2.add_money(20)

#print(aldis.get_total_balance())
#print(banka.get_total_deposits())