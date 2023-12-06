"""Task 7: Bank account."""

class BankAccount():
    """A class that represents a bank account."""
    
    # TODO: Code has been removed from here. 


"""Task 10: Overdraft account."""

class OverdraftAccount(BankAccount):
    """A class that represents a bank account allowing overdraft."""
    
    # TODO: Code has been removed from here. 

if __name__ == '__main__':
    # Task 7
    my_account = BankAccount(1000)
    my_account.print_balance()
    my_account.deposit(500)
    my_account.print_balance()
    my_account.withdraw(200)
    my_account.print_balance()
    my_account.withdraw(2000)
    my_account.print_balance()

    # Task 10
    #my_account = OverdraftAccount(0, 500)
    #my_account.print_balance()
    #my_account.deposit(1000)
    #my_account.print_balance()
    #my_account.withdraw(1300)
    #my_account.print_balance()
    #my_account.withdraw(500)
    #my_account.print_balance()    
