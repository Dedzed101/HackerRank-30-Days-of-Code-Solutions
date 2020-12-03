# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
        #Cast user input as a float or a variable
        meal_cost = float(input())
        tip_percent = int(input())
        tax_percent = int(input())
        
        #Calculate tip, tax, and total. Return
        tip = ((tip_percent/100)*meal_cost)
        tax = ((tax_percent/100)*meal_cost)
        total_cost = meal_cost + tip + tax
        
        return(round(total_cost)) 

#Print returned value with placeholder inputs
print(solve(12.0, 2, 3))