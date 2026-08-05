def countVowel(string):
    count = 0
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1
    return count

word = "Adventure Time"
print(f"The number of vowels in '{word}' is: {countVowel(word)}")
