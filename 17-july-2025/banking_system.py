# Bank Account System using OOP Concepts

class BankAccount:

    interest_rate = 0.05

    def __init__(self, account_num, balance, account_holder_name):
        self.__account_num = account_num
        self.__balance = balance
        self.__account_holder_name = account_holder_name

    @property
    def get_account_num(self):
        return self.__account_num

    @property
    def get_account_holder_name(self):
        return self.__account_holder_name

    """To deposit the money"""
    def deposit(self, new_balance):
        val_acc_num = input("Enter your account number: ")
        val_acc_name = input("Enter your account name: ")
        if (self.__account_num == val_acc_num) and (self.__account_holder_name == val_acc_name):
            if new_balance < 0:
                raise ValueError("The balance to be deposited can't be less than zero")
            else:
                self.__balance = self.__balance + new_balance
        else:
            print("Account details don't match")
        return new_balance

    """To withdraw the money"""
    def withdraw(self, withdrawal_amt):
        val_acc_num = input("Enter your account number: ")
        val_acc_name = input("Enter your account name: ")
        if (self.__account_num == val_acc_num) & (self.__account_holder_name == val_acc_name):
            self.__balance = self.__balance - withdrawal_amt
        else:
            print("Account details don't match")
        return self.__balance

    @classmethod
    def get_loan(cls, loan_amt):
        if loan_amt < 0:
            raise ValueError("Loan Amount can not be less than zero")
        else:
            interest_amt = loan_amt * cls.interest_rate
            total_to_pay = loan_amt+interest_amt
            print(f'Loan Amount: Rs. {loan_amt}\n'
                  f'Interest Rate: {interest_amt}\n'
                  f'Total Amount to be paid: Rs. {total_to_pay}')

    """To check the current balance"""
    @property
    def check_balance(self):
        return self.__balance

    def acc_summary(self):
        print(f'Account Details\n'
              f'Account Number: {self.__account_num}\n'
              f'Account Holder Name: {self.__account_holder_name}\n'
              f'Account Balance: {self.__balance}\n')

class SavingsAccount(BankAccount):
    interest_rate = 0.08

    def __init__(self, account_num, balance, account_holder_name, min_balance=500):
        super().__init__(account_num, balance, account_holder_name)
        self.__min_balance = min_balance

    def get_min_balance(self):
        return self.__min_balance

    # @classmethod
    def set_min_balance(self, value):
        if value < 0:
            raise ValueError("Enter a positive amount")
        else:
            self.__min_balance = value


    def monthly_withdrawal(self, withdrawal_amt):
        val_acc_num = input("Enter account number: ")
        val_acc_name = input("Enter the account holder name: ")

        if (val_acc_num == self.get_account_num) and (val_acc_name == self.get_account_holder_name):
            if self.check_balance - withdrawal_amt < self.__min_balance:
                print("Can't withdraw money! Must withdraw a minimum balance")
            else:
                super().withdraw(withdrawal_amt)

        if withdrawal_amt > 25000:
            print("You can't withdraw more than 25k per month")

    def apply_interest(self):
        interest = self.check_balance * self.interest_rate
        self.deposit(interest)
        print(f'Interest of Rs. {interest} deposited in the account')

    def acc_summary(self):
        print(f'Account Details\n'
              f'Account Number: {self.get_account_num}\n'
              f'Account Holder Name: {self.get_account_holder_name}\n'
              f'Account Balance: {self.check_balance}\n'
              f'Minimum Balance: {self.__min_balance}\n'
              f'Account Interest: {self.interest_rate * 10}%\n')

class Taxable(BankAccount):
    tax_rate = 0.1 # 10%

    def calculate_tax(self):
        return self.check_balance * self.tax_rate

class Insured:
    def __init__(self, insurance_amt):
        self.__insurance_amt = insurance_amt

    def display_insurance(self):
        print(f"Insurance Amount is: {self.__insurance_amt}")

class PremiumSavingsAccount(SavingsAccount, Taxable, Insured):

    def __init__(self, account_num, balance, account_holder_name, min_balance=5000, insurance_amt = 100000):

        SavingsAccount.__init__(self, account_num, balance, account_holder_name, min_balance)
        Insured.__init__(self, insurance_amt)

        self.interest_rate = 0.9

    def premium_acc_summary(self):
        print(f'Premium Account Details\n')
        print(self.acc_summary())
        print(f"Tax Liability: Rs. {self.calculate_tax()}\n")
        self.display_insurance()

premium_acc = PremiumSavingsAccount('123456789', 600000, 'Sania')
premium_acc.acc_summary()
premium_acc.deposit(10000)
premium_acc.acc_summary()
premium_acc.withdraw(5000)
premium_acc.acc_summary()
premium_acc.calculate_tax() # tax to be implemented is Rs. 60,500
# premium_acc.acc_summary()
# print(premium_acc.display_insurance())
premium_acc.premium_acc_summary()

#
# acc1 = BankAccount('123456789', 56000, 'Sania')
# acc1.acc_summary()
# acc1 = SavingsAccount('123456788', 60000, 'Sania', 2000)
# acc1.acc_summary()
# acc1.acc_summary()