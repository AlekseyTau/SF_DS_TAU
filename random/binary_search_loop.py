def search_predict(number: int = 1) -> int:

    count = 0
    low = 0
    high = 100

    while low <= high:  
        mid = (low + high) // 2  # Calculate the mid

        if mid == number:  # Check if the middle element matches the target number
            count += 1
            break  # Exit the loop if the number is found
        elif mid < number:
            low = mid + 1  # Adjust the low index for the next iteration
        else:
            high = mid - 1  # Adjust the high index for the next iteration


        count +=1


    return count
        
print(search_predict(5))