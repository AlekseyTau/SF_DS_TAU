'''Guess the number
But computer here are both, the enigmatic and the guesser
'''

import numpy as np


def random_predict(number: int=1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: atempt count
    """
    count = 0 
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101) # assumed number
        if number == predict_number:
            break # exit the cycle if guessed right
    return(count)

def score_game(number_predict) -> int:
    """Counting average attemps to guess the number in 1000 numbers

    Args:
        number_predict (_type_): The guessing func

    Returns:
        int: The mean quantity of guesses to succes
    """
    
    count_list = []
    
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # set list of numbers
    
    for number in random_array:
        count_list.append(random_predict(number))
        
    score = int(np.mean(count_list))
    print(f'Your algoryhm will guess in {score} attempts average')
    return(score)

# RUN

if __name__ == '__main__':
    score_game(random_predict)
    

