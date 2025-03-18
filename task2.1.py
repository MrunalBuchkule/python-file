def count_vowels_and_consonants(sentence):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in sentence:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count

def main():
    
    sentence = input("Enter a sentence: ")

    title_case_sentence = sentence.title()
    print(f"\nTitle Case: {title_case_sentence}")


    words = sentence.split()
    total_words = len(words)
    print(f"\nTotal number of words: {total_words}")


    vowels, consonants = count_vowels_and_consonants(sentence)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")


    reversed_sentence = sentence[::-1]
    print(f"\nReversed sentence: {reversed_sentence}")


main()
