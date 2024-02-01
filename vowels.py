def main():
    user_input = str(input("Enter the string "))
    print(count_vowels(user_input))


def count_vowels(text: str) -> int:
    vowel_count = 0
    text = text.lower()
    vowels = ["a", "e", "i", "o", "u"]
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count


main()
