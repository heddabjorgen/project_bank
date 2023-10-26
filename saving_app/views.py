from django.shortcuts import render, redirect
from saving_app.models import SavingsAccount
from rest_framework.response import Response
from saving_app.serializer import SavingsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1 style='font-family: Arial, sans-serif; font-weight: bold; text-align: center;'>Welcome to the savings app, this is where your dreams start!</h1><p style='font-family: Arial, sans-serif; text-align: center;'> Use http://127.0.0.1:8000/ + account/, update/id, my_goals/id to make changes to your account. Read readme.txt for more info</p>")

#To see all accounts
@api_view(["GET"])
def get_account(request):
    account = SavingsAccount.objects.all()
    serializer = SavingsSerializer(account, many=True)
    return Response(serializer.data,
                    status = status.HTTP_200_OK)

#To create a new account and save it
@api_view (["POST"])
def save_account(request, id):
    serializer = SavingsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)



#To deposit money using an API and the deposit_amount function from models
@api_view(["PUT"])
def update_account(request, id):
    try:
        theAccount = SavingsAccount.objects.get(pk=id)
    except SavingsAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    deposit_amount = float(request.data.get("deposit_amount", 0))

    if deposit_amount <= 0:
        return Response({"error": "Deposit amount must be a positive number greater than 0."}, status=status.HTTP_400_BAD_REQUEST)

    theAccount.deposit(deposit_amount)
     
    reward_or_cheer = ""
    if deposit_amount >= 1000:
        reward_or_cheer = "You are a savings star! With these deposists frequently the stars is the limit!"
    elif deposit_amount >= 500:
        reward_or_cheer = "You know what we say about saving? The more the money has to work for you, the less you have to work for the money"
    else:
        reward_or_cheer = "Awesome! Did you know that saving 100 kr a week for two years will provide your next holiday with 10400 kr + interest rate? Keep on!"

    serializer = SavingsSerializer(theAccount, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Deposit successful", "reward_or_cheer": reward_or_cheer, "updated_data": serializer.data})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def check_savings_goal_message(request, id):
    try:
        theUser = SavingsAccount.objects.get(id=id)
    except SavingsAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    get_goal = float(request.data.get("get_goal", 0))

    if get_goal <= 0:
        return Response({"error": "You can do better, your goal should be more than 0."}, status=status.HTTP_400_BAD_REQUEST)

    message = theUser.check_savings_goal(get_goal)

    return Response({"message": message})           
            