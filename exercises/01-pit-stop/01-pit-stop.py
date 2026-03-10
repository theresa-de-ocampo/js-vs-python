# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

total_race_time = float(input("Total Race Time (s): "))
pit_stops = int(input("How many pit stops were made? "))
ave_pit_stop_time = float(input("Ave. Pit Stop Duration (s): "))

total_pit_stop_time = ave_pit_stop_time * pit_stops
pit_stop_percent = round((total_pit_stop_time / total_race_time) * 100, 2)

print("\n--- Pit Stop Summary ---")
print(f"Total Pit Stop Time (s): {total_pit_stop_time}")
print(f"Percentage of Race in Pits: {pit_stop_percent}%")

if pit_stop_percent > 5:
    print("You need a new pit crew. 🛠️")
