# 1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times).

import random

count_6 = 0
count_1 = 0
consecutive_6s = 0

# Keep track of the previous roll to check for "two 6s in a row"
previous_roll = None

print("Rolling the die 20 times...")

for i in range(20):
    current_roll = random.randint(1, 6)
    print(f"Roll {i+1}: {current_roll}")
    
    if current_roll == 6:
        count_6 += 1
        
    if current_roll == 1:
        count_1 += 1
        
    if current_roll == 6 and previous_roll == 6:
        consecutive_6s += 1
        
    previous_roll = current_roll

# Print final statistics
print("\n--- Statistics ---")
print(f"Number of times 6 was rolled: {count_6}")
print(f"Number of times 1 was rolled: {count_1}")
print(f"Number of times two 6s were rolled in a row: {consecutive_6s}")

# 2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.

# Set the total workout target and the number of jumping jacks per set
TOTAL_TARGET = 100
SET_SIZE = 10

completed_jacks = 0

print(f"Goal for today: {TOTAL_TARGET} jumping jacks!")

# Loop through the sets until the target is reached
while completed_jacks < TOTAL_TARGET:
    completed_jacks += SET_SIZE
    print(f"\nPerform {SET_SIZE} jumping jacks! (Total done: {completed_jacks})")
    
    # If the user reaches the total target, the workout finishes automatically
    if completed_jacks >= TOTAL_TARGET:
        break
        
    # Ask if the user is tired
    tired = input("Are you tired? ").strip().lower()
    
    if tired in ['yes', 'y']:
        # Ask if they want to skip the remaining sets
        skip = input("Do you want to skip the remaining sets? ").strip().lower()
        if skip in ['yes', 'y']:
            break  # Stop the workout early
            
    elif tired in ['no', 'n']:
        # Calculate and display how many jumping jacks are remaining
        remaining = TOTAL_TARGET - completed_jacks
        print(f"{remaining} jumping jacks are remaining.")

# Determine the final message based on how the loop ended
if completed_jacks >= TOTAL_TARGET:
    print("\nCongratulations! You completed the workout.")
else:
    print(f"\nYou completed a total of {completed_jacks} jumping jacks.")
