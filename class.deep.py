print("ENCAPSULATION ")

'''
C++ java > public private protected 
php typescript > public private protected 
python > name <public  __name < protected  _name
__name__ <dunder 
'''


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership", new_owner)
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("-------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("-------")
'''
my_account.amount = 10000000
my_account.owner = "Martin"
my_account.amount = 100000000
my_account.get_balance()

'''
try:
    result = my_account.amount
    print("result", result)
except Exception as err:
    pass
    print("no target state found", err)

print(" owner before", my_account.holder)  # state
# my_account.change_ownership("martin")
my_account.holder = "martin"
print(" owner after", my_account.holder)
