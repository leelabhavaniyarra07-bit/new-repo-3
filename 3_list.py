justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Step 1: Calculate the number of members
print("Step 1: Initial list")
print(justice_league)
num_members = len(justice_league)
print("Number of members:", num_members)
print()

# Step 2: Batman recruited Batgirl and Nightwing -> add them to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Step 2: After adding Batgirl and Nightwing")
print(justice_league)
print()

# Step 3: Wonder Woman is now the leader -> move her to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Step 3: After making Wonder Woman the leader")
print(justice_league)
print()

# Step 4: Aquaman and Flash are having conflicts -> separate them by
# inserting either "Green Lantern" or "Superman" between them
chosen_separator = "Green Lantern"  # or could be "Superman"
justice_league.remove(chosen_separator)  # remove it from its current spot first

flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")

# Insert the separator right after whichever of the two comes first
insert_index = min(flash_index, aquaman_index) + 1
justice_league.insert(insert_index, chosen_separator)

print(f"Step 4: After separating Aquaman and Flash with '{chosen_separator}'")
print(justice_league)
print()

# Step 5: Crisis! Superman assembles a brand new team -> replace the list entirely
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Step 5: New team assembled by Superman")
print(justice_league)
print()

# Step 6: Sort alphabetically -> hero at index 0 becomes the new leader
justice_league.sort()
new_leader = justice_league[0]
print("Step 6: Sorted alphabetically")
print(justice_league)
print("New leader:", new_leader)
print()

# BONUS: Predicting the new leader
# Sorting alphabetically means whichever name comes first in the alphabet wins.
# Comparing the 5 new members: Cyborg, Green Arrow, Hawkgirl, Martian Manhunter, Shazam
# "Cyborg" starts with 'C', which comes before G, H, M, and S -> Cyborg was predictable
# as the new leader before even running the sort.
print("BONUS prediction: 'Cyborg' will be the new leader (starts with 'C', earliest alphabetically).")
