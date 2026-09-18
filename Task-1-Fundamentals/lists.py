justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# count members
members = len(justice_league)
print(f"There are total {members} in justice league")
print(justice_league)

# added nightwing and batgirl
justice_league.append("Nightwing")
justice_league.append("Batgirl")
print(justice_league)

# Made wonder woman leader
leader = justice_league.pop(2)
justice_league.insert(0, leader)
print(justice_league)

# Added Superman between Aquaman and flash
superman = justice_league.pop(1)
justice_league.insert(3, superman)
print(justice_league)

# Replace old team with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)

# Sort the Justice League alphabetically
justice_league.sort()
# Cyborg would become the new leader
print(justice_league)