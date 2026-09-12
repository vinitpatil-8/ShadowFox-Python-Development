justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# count members
members = len(justice_league)
print(f"There are total {members} in justice league")

# added nightwing
justice_league.append("Nightwing")

# Made wonder woman leader
leader = justice_league.pop(2)
justice_league.insert(0, leader)

# Added Superman between Aquaman and flash
superman = justice_league.pop(1)
justice_league.insert(3, superman)

# Replace old team with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)