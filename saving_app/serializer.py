from rest_framework import serializers 
from saving_app.models import SavingsAccount



class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsAccount
        fields = ['id', 'user', 'account_number', 'balance']

