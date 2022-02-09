John likes to go to the cinema. He can choose between system A and system B.

System A : He buys a ticket (15 dollars) every time


System B : He buys a card (500 dollars) and a first ticket for 90% of a normal ticket price (15 dollars). 
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

The function movie has 3 parameters: card (price of the card), ticket (normal price of a ticket), perc (fraction of what he paid for the previous ticket) and returns the first n such that

ceil(price of System B) < price of System A.
More examples:
movie(500, 15, 0.9) should return 43 
    (with card the total price is 634, with tickets 645)
movie(100, 10, 0.95) should return 24 
    (with card the total price is 235, with tickets 240)
