sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []

sales_w2_d7 = int(input("Sales for Week 2, Day 7: "))
sales_w2.append(sales_w2_d7)

sales = sales_w1 + sales_w2
highest_sales = max(sales)
lowest_sales = min(sales)

PROFIT = 1.5

highest_profit = round(highest_sales * PROFIT, 2)
lowest_profit = round(lowest_sales * PROFIT, 2)
total_hl = round(highest_profit + lowest_profit, 2)

print(f"Highest Profit: ${highest_profit:.2f}")
print(f"Lowest Profit: ${lowest_profit:.2f}")
print(f"Highest + Lowest Profit: ${total_hl:.2f}")
