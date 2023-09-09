"""5) 1.	Реализуйте класс Client, представляющий клиента банка. Класс должен иметь атрибуты name (имя клиента)
и id (уникальный идентификатор клиента).
2.	Реализуйте класс BankAccount, представляющий банковский счет. Класс должен иметь атрибуты account_number
(номер счета), balance (баланс счета) и client (объект типа Client, которому принадлежит счет). Класс также
должен иметь методы deposit(amount) и withdraw(amount), которые позволяют пополнить или снять деньги со счета.
3.	Реализуйте класс Bank, представляющий банк. Класс должен иметь атрибут accounts, который является словарем,
где ключами являются номера счетов, а значениями - объекты типа BankAccount. Класс также должен иметь методы
create_account(client, initial_balance) для создания нового счета и get_account(account_number) для получения
счета по его номеру.
4.	Добавьте в класс Bank методы для выполнения переводов между счетами (transfer(sender_account, receiver_account,
amount)), а также для получения общего баланса клиента (get_total_balance(client)), который включает сумму денег
на всех его счетах.
5.	Реализуйте обработку ошибок, например, недостаточно средств на счете при снятии денег или отсутствие счета
при переводе."""


class Client:
    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.client = client.id_

    def deposit(self, amount1):
        total_balance = self.balance + amount1
        return f"Счет пополнен на сумму: {amount1}. {client.name}, Ваш баланс на счету '{self.client}' - " \
               f"{total_balance} рублей"

    def withdraw(self, amount2):
        if amount2 < self.balance:
            account_balance = self.balance - amount2
            return f'Остаток на балансе: {account_balance}'
        else:
            return f"Недостаточно средств. {client.name}, Ваш баланс на счету '{client.id_}' - {self.balance}"


client = Client('Andrei', '876dhj')
# client2 = Client('Kate', '9039k')
bank_account = BankAccount('5u', 156)
print(bank_account.withdraw(200))
print(bank_account.deposit(300))


class Bank:
    accounts = {bank_account.account_number: bank_account.balance}

    def create_account(self, client_account_number, initial_balance):
        self.accounts[client_account_number] = initial_balance
        return f"Поздравляем, счет успешно создан! Ваши текущие счета: {self.accounts}"

    def get_account(self, account_number):
        if account_number in self.accounts:
            return f"Ваш баланс на счету '{account_number}' составляет {self.accounts[account_number]}"
        else:
            return f"Счета '{account_number}' не существует"

    def transfer(self, sender_account, receiver_account, amount):
        if self.accounts[sender_account] > amount:
            self.accounts[receiver_account] = self.accounts[receiver_account] + amount
            self.accounts[sender_account] = self.accounts[sender_account] - amount
            return f"Перевод на сумму {amount} выполнен успешно. Ваш баланс: {self.accounts[sender_account]}"
        else:
            return f"Недостаточно средств для перевода. Ваш баланс - {self.accounts[sender_account]}"

    def get_total_balance(self, client):
        self.client = client.name
        total = sum(self.accounts.values())
        return f'{self.client}, общая сумма на Ваших счетах составляет {total}'


bank = Bank()
bank.create_account('2d3', 600)
bank.create_account('84nf', 983)
print(bank.create_account('15g', 6280))
print(bank.get_account('84nf'))
print(bank.transfer('2d3', '84nf', 1000))

print(bank.get_total_balance(client))
