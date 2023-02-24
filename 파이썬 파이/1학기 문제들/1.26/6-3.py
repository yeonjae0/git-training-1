vowel = ['a', 'e', 'i', 'o', 'u']

def count_vowels(word):
    cnt = 0
    for i in word:
        if i in vowel:
            cnt += 1
    return print(cnt)

count_vowels('apple') #=> 2
count_vowels('banana')