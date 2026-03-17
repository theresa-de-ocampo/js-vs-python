# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
# purchases = [3.75, 7.20, 3.25, 2.65, 10, 2.95, 12, 2.5]
total_spent = round(sum(purchases), 2)
total_points = 0


def earn_points(price):
    return int(price) * 3


def tier_label(points):
    tier = "Gold"

    if points < 100:
        tier = "Bronze"
    elif points < 500:
        tier = "Silver"

    return tier


for amount in purchases:
    total_points += earn_points(amount)

tier = tier_label(total_points)
print("Loyalty Summary")
print(f"Total dollars spent: ${total_spent:.2f}")
print(f"Total points earned: {total_points}")
print(f"Final tier: {tier}")
