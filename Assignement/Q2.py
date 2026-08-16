scores = tuple(L[:8])

print("Scores:", scores)

highest = max(scores)
highest_index = scores.index(highest)

print("Highest score:", highest)
print("Index of highest score:", highest_index)

lowest = min(scores)
lowest_count = scores.count(lowest)

print("Lowest score:", lowest)
print("Lowest score appears:", lowest_count, "times")

reverse_scores = list(scores[::-1])

print("Reversed tuple as list:", reverse_scores)

search = int(input("Enter a score to search: "))

if search in scores:
    print("First occurrence index:", scores.index(search))
else:
    print("Score is not present.")

print("Trying to change the tuple...")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

first, second, *remaining = scores

print("First score:", first)
print("Second score:", second)
print("Remaining scores:", remaining)
