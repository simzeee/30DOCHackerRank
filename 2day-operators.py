def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    total = (tip_percent/100)*meal_cost + (tax_percent/100)*meal_cost + meal_cost
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
