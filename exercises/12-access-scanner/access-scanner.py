# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

REVOKED_BADGE_NUMBERS = {11, 21, 31, 41, 51}
approved = []
denied = []


while True:
    name = input("\nName (or type 'done' to exit): ").title()

    if name == "Done":
        break

    badge_number = int(input("Badge Number: "))

    if badge_number in REVOKED_BADGE_NUMBERS:
        denied.append(name)
        print("ACCESS DENIED")
    else:
        approved.append(name)
        print("ACCESS GRANTED")

print("\n✅ Approved Visitors")
for approved_visitor in sorted(approved):
    print("\t", approved_visitor)
print(f"Total Approved Visitors: {len(approved)}")

print("\n⛔️ Denied Visitors")
for denied_visitor in sorted(denied):
    print("\t", denied_visitor)
print(f"Total Denied Visitors: {len(denied)}")
