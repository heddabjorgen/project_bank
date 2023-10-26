from django.db import models

class SavingsAccount(models.Model):
    user = models.CharField(max_length = 50, default = "default user")
    account_number = models.CharField(max_length = 50)
    balance = models.FloatField(default=0)
    
    def __str__(self):
        return f"{self.user} - {self.account_number} - {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        self.save()
        return True
    
    def check_savings_goal(self, goal):
        if goal <= self.balance:
                return "Congratulations! You've reached your savings goal!"
        else:
            return f"Keep saving! You are {goal - self.balance} away from your goal. You know what they say, Do not save what is left after spending, but spend what is left after saving"

