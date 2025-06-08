food = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
letter = input("Enter the letter for which the search is to be done: ")
matches = []
for x in food:
    if x.startswith(letter):
        matches.append(x)
print(matches)

