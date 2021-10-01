import random
import string

adjectives = ['sleepy', 'slow', 'smelly',
              'wet', 'fat', 'red',
              'hairy', 'strange', 'cruel'
              'fluffy', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda',
         'telephone', 'banana', 'teacher']

colours = ['red', 'green', 'yellow',
           'blue', 'purple', 'orange',
           'brown', 'black', 'white']

print("Welcome to Password Picker!")

while True:

    for num in range(3):
        adjective = random.choice(adjectives)
        colour = random.choice(colours)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + colour + noun + str(number) + special_char
        print(f'Your new password is: {password}')

    response = input('Would you like another password? y/n ')
    if response == 'n':
        break
    
