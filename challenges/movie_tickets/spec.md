John likes to go to the cinema. He can choose between system A and system B.

System A : He buys a ticket (15 dollars) every time


System B : He buys a loyalty card (500 dollars) and the first ticket for 90% of a normal ticket price (15 dollars). 
Then, for each additional ticket he pays 90% of price he paid for the previous ticket.


Example:
If John goes to the cinema 3 times:

System A : 15 * 3 = 45

System B : 
1st ticket = 15 * 0.90 = 13.5

2nd ticket = 13.5 * 0.90 = 12.15

3rd ticket = 12.15 * 0.90 = 10.935

Ticket Total = 13.5 + 12.15 + 10.935 = 36.585

Ticket Total + Card (500) = 500 + 36.585 = 536.585

**John wants to know how many tickets he must buy using system B for it to be a cost effective choice when compared to buying tickets using system A. 

Write a function called movie that takes 3 parameters: loyalty_card (price of the loyalty card), ticket (normal price of a ticket), discount (the discount applied to the ticket price when using system B), and returns the number of tickets John must buy for it to be worth buying the loyalty card. 

Printing the working function should look like this:


print(movie(500, 15, 0.9)) #should return 43 with the system B giving a total price is 634 and system A giving a total price of 645

print(movie(100, 10, 0.95)) #should return 24 with the system B giving a total price is 235 and system A giving a total price of 240
