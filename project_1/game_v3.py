"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np



def search_predict(number: int = 1) -> int:
    """The alhorythm for search the guessed number in range form 1 to 100

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: Ammount of attempts to guess
    """

    count = 0
    low = 0
    high = 100  

    while low <= high:  # Set the condition for loop
        mid = (low + high) // 2  # Calculate the mid index

        if mid == number:  # Check if the middle element matches the target number
            count += 1
            break  # Exit the loop if the number is found

        elif mid < number:
            low = mid + 1  # Adjust the low index for the next iteration
        else:
            high = mid - 1  # Adjust the high index for the next iteration

        count +=1

    return count
        


def score_game(search_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(search_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(search_predict)
