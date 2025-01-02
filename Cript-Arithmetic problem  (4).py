from itertools import permutations

def solve_cryptarithm(words):
    unique_letters = set("".join(words))
    
    if len(unique_letters) > 10:
        return "Too many unique letters to solve (more than digits)."
    
    for perm in permutations(range(10), len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, perm))
        if any(letter_to_digit[word[0]] == 0 for word in words):
            continue
        
        values = [int("".join(str(letter_to_digit[letter]) for letter in word)) for word in words]
        
        if sum(values[:-1]) == values[-1]:
            return {
                "Words": {word: values[i] for i, word in enumerate(words)},
                "Mapping": letter_to_digit
            }
    
    return "No solution found."

words = input("Enter the words:\n ").split()
result = solve_cryptarithm(words)
print(result)
