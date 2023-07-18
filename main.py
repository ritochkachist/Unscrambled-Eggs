# 7/17/2023
# Margarita Chistiakova


from re import sub
def unscramble_eggs(word):
    return sub(r'([^aieou])egg',r'\1', word)

print("Please enter a word of a phrase writing 'egg' after every consonant: ")
word = input()
print("I am going to remove all the 'egg' parts from the phrase you gave")
result = unscramble_eggs(word)
print(result)
