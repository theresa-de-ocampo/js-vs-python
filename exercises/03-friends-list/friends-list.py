csv = "Eric,John,Michael,Terry,Graham:TerryG;Brian"
csv = csv.replace(":", ",").replace(";", ",")
friends_list = csv.split(",")
print(friends_list)
