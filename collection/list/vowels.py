# words starting with vowels

words=["apple","orange","potatto","iphone","tomatto"]

vowels=["a","e","i","o","u"]

vowels_words=[i for i in words if i[0]in vowels]

print(vowels_words)

consonant_words=[i for i in words if i[0]not in vowels]

print(consonant_words)

# longest word

longest=max([len(i) for i in words ])

longest_word=[i for i in words if len(i)==longest]

print(longest_word)