def twoSum(nums, target):
    """
    Given an array of integers `nums` and an integer `target`, 
    return indices of the two numbers such that they add up to `target`.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[int]: Indices of the two numbers that add up to `target`.
    """
    # Dictionary to store the value and its index
    num_map = {}
    
    # Iterate over the list with index and value
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        
        # If the complement exists in the dictionary, return the indices
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store the index of the current number in the dictionary
        num_map[num] = i
    
    # Return an empty list if no solution is found
    return []