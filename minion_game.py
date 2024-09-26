# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


#                               Answer
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV














def score_calc(string, substring):
    score = 0
    substring_length = len(substring)   
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == substring:
            score += 1           
    return score

if __name__ == '__main__':
    score_final = 0
    while True:
        string = input('Enter a string under 10 characters in length: ')
        if len(string) <= 10:
            break
        else:
            print('Max size is 10 letters')
    while True:
        guess = input('Enter a substring (or type "exit" to quit): ')
        if guess.lower() == "exit":
            break
        if len(guess) > 0:
            if guess in string:
                occurrences = score_calc(string, guess)
                print(f"{guess} exists {occurrences} time(s) in '{string}'.")
                score_final += occurrences
            else:
                print(f"{guess} doesn't exist in '{string}'.")
        else:
            print("Please enter a valid substring.")
    print(f"Total score: {score_final}")
