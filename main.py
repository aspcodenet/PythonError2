
from enum import Enum

class WithdrawalError(Enum):
    TooLowBalance = 1
    NotMoreThan2000 = 2
    Ok = 3


class Player:
    def __init__(self,age):
        if age < 0:
            raise ValueError("Bla bla") # GOD OOP
        self.__age = age

try:
    a = Player(-12)
except:
    pass

print(a)

class BankAccount:
    def __init__(self, kontonummer:str):
        self.__saldo = 0
        self.__kontonummer = kontonummer

    def Deposit(self, belopp:int):
        self.__saldo = self.__saldo + belopp

    def Withdraw(self, belopp:int):
        if belopp > self.__saldo: 
            #raise ValueError("Too low balance")
            return WithdrawalError.TooLowBalance
        if belopp > 2000: # max 2000 per uttag
            return WithdrawalError.NotMoreThan2000
            #raise ValueError("Not more than 2000 per time")
        self.__saldo = self.__saldo - belopp
        #Save transaction - skulle kunna skita sig
        # nätverksuppkoppling -> banken - skulle kunna skita sig
        #return True
        return WithdrawalError.Ok




a = BankAccount("12345")        
a.Deposit(5000)

ok = a.Withdraw(3500)


			# jättebra! Vi kan uttrycka ALLT och hantera ALLT
			# Särskilja olika typer av fel och förmedla till anv osv
            # hantera . recover i olika fall
			# Utan att krascha
# TENTA - felhantering (nmi behöbver inte tänka på return enum):
# try 
# med många except-rader som hanterar OLIKA typer av exceptions
# raise ( = ensure valid state)
# typexempel: def __init__  good OOP


try:
    ok = a.Withdraw(2500)
except ValueError as ex:    
    print(ex)
except:
    print("Ngt gick jättefel")
    # reboot bankomat


                    