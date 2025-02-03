class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


LEGAL_AGE = 18
input_data = input().split(', ')
pin = int(input_data[0])
balance = float(input_data[1])
age = int(input_data[2])

command = input()
while command != 'End':
    cmd_details = command.split('#')
    current_command = cmd_details[0]
    money = float(cmd_details[1])

    if current_command == 'Send Money':
        provided_pin = int(cmd_details[2])

        if age < LEGAL_AGE:
            raise UnderageTransactionError('You must be 18 years or older to perform online transactions')

        if balance < money:
            raise MoneyNotEnoughError('Insufficient funds for the requested transaction')

        if pin != provided_pin:
            raise PINCodeError('Invalid PIN code')

        balance -= money
        print(f'Successfully sent {money:.2f} money to a friend')
        print(f'There is {balance:.2f} money left in the bank account')

    elif current_command == 'Receive Money':
        if money < 0:
            raise MoneyIsNegativeError('The amount of money cannot be a negative number')

        money_received = money / 2
        balance += money_received
        print(f'{money_received:.2f} money went straight into the bank account')

    command = input()
