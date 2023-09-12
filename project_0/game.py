import numpy as np
number = np.random.randint(1, 101) # set the number

# attempt count
count = 0
while True:
    
    count += 1
    predict_number = int(input('Guess the number from 1 to 100:'))
    
    if predict_number > number:
        print('The number should be less')
    elif predict_number < number:
        print('The number should be bigger')
    else:
        print(f"Right guess! It's {number} Congratulations! It took you {count} attempts!")
        break # Stop if guessed right
    
    