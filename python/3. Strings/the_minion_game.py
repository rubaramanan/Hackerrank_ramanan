def minion_game(string):
    vowels = "AEIOU"
    stuart_score = 0  # Consonant player
    kevin_score = 0  # Vowel player
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin_score += (n - i)  # Vowel contributes to Kevin's score
        else:
            stuart_score += (n - i)  # Consonant contributes to Stuart's score

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)