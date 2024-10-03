'''
4) A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
program:
# Input: Total cost of a dozen bananas (X) and selling price of one banana (Y)
cost_price = float(input())
selling_price_per_banana = float(input())

# Calculate the total selling price for a dozen bananas
total_selling_price = selling_price_per_banana * 12

# Calculate profit or loss
profit_loss = total_selling_price - cost_price

# Output: Profit or Loss
if profit_loss > 0:
    print(f"Profit : Rs.{profit_loss:.2f}")
elif profit_loss < 0:
    print(f"Loss : Rs.{-profit_loss:.2f}")
else:
    print("No Profit No Loss")
'''
