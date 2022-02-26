print('Welcome to the Magic 8 Ball')

Operation = input('What would you like me to do? (Tell a joke, Pick a number, Flip a coin) ')

import random
if Operation == 'Flip':
    flip = random.randint(0, 1)
    if flip == 0:
        print('You got heads')
    elif flip == 1:
        print('You got tails')
elif Operation == 'number' or Operation == 'Number':
    print(random.randint(1,10))

elif Operation == 'joke' or Operation == 'Joke':
    import pyjokes
    joke1 = pyjokes.get_joke(language='en', category= 'all')
    print(joke1)
