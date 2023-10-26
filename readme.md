## Task description
> Short description of my project.
👩🏽‍💻🏦

In this Savings Account Challenge, my primary focus was on creating a robust API that facilitates various operations related to managing savings accounts. The core tasks I focused on was designing models to represent user accounts, implementing functionalities for depositing funds into accounts, letting the user set savings goals, and providing feedback messages based on user-defined goals and current savings balances.

Additionally, I made endpoints to support operations such as creating new accounts, and updating information. Throughout the project, my aim was to ensure seamless communication between the frontend and backend by using a REST API principles and integrating appropriate error handling mechanisms with Django framework and relational database.

However in addition to the mechanism, I tried to make it fun for the user to use by providing feedback on deposits and goals - so that the user experience would be more fun. All in all, I aimed to develop a user-friendly savings management system that promotes financial awareness and encourages users to achieve their savings goals efficiently.



## How to run
> Instructions!

Installitions:
--> pip3 install djangorestframework
--> pip3 install django

How to run server:
-->Open the project in Visual Studio Code
-->Open the terminal in Visual Studio Code and type in: source env/bin/activate
-->Then python manage.py runserver

After entering the server:

To make a deposit to Ibens account:
http://127.0.0.1:8000/update/2

Enter this, and try different deposit amounts:

{
 "account_number": "121314151617"
, "deposit_amount": 50 
}


To make a saving goal:
http://127.0.0.1:8000/my_goals/2

Enter this and choose an amount:

{ 
"get_goal": 60000 
}

To view all accounts:
http://127.0.0.1:8000/account


You can also create new accounts with this link(with a new unique id at the end):
http://127.0.0.1:8000/account/id

In this format:

{ 
"user": "John Doe",
"account_number": "4567890876",
"balance": 5000 
}

Feel free to try different things! 😇

## Comments
I hope you like my project! Let me know if you have any quetions.
