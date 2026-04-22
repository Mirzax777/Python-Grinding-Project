def find_vowels(words):
    results = []
    for word in words:
        for letter in word:
            if letter.lower() in 'aeiou':
                results.append((word, letter))
                break
        else:
            results.append((word, None))
    return results


if __name__ == '__main__':
    words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
    for word, vowel in find_vowels(words):
        if vowel:
            print(f"'{word}' contains the vowel '{vowel}'")
        else:
            print(f"'{word}' has no vowels")
