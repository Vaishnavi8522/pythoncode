# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:30:52 2024

@author: vaip8
"""

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")

    def get_balance(self):
        return self.balance