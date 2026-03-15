names = ["john ClEEse", "Eric IDLE", "michael"]
names1 = ["graHam chapman", "TERRY", "terry jones"]

names1.append(input("First Additional: "))
names1.append(input("Second Additional: "))

invitees = set(name.capitalize() for name in names + names1)

print("\n")
for invitee in invitees:
    print(f"{invitee.title()}! You are invited to the party on Saturday.")
