class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit) -> None: # Constructor
        """Create a new credit card instance.
        The initail balance is zero.
        
        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._balance = 0
        self._limit = limit

    def get_customer(self):
        """Return name of the customer."""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name."""
        return self._bank
    
    def get_account(self):
        """Return the card identifying numer (typically stored as a string)."""
        return self._acnt
    
    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

class PrdatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees.
    
    customer    the name of the customer (e.g., 'John Bowman')
    bank        the name of the bank (e.g., 'California Savings')
    acnt        the account identifier (e.g., '5391 0375 9387 5309')
    limit       Credit card limit (measured in dollars)
    apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """

    def __init__(self, customer, bank, acnt, limit, apr) -> None:
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied"""

        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""

        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance += monthly_factor



if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print(f'Customer = {wallet[c].get_customer()}')
        print(f'Bank = {wallet[c].get_bank()}')
        print(f'Account = {wallet[c].get_account()}')
        print(f'Limit = {wallet[c].get_limit()}')
        print(f'Balance = {wallet[c].get_balance()}')
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f'New balance = {wallet[c].get_balance()}')
        print()