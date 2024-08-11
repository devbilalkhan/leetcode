def containsDuplicate(nums):
    """
    Function to check if there are any duplicates in the list.
    
    :type nums: List[int]
    :rtype: bool
    """
    # Initialize an empty set to store unique items
    unique_items = set()
    
    # Iterate through each value in the list
    for value in nums:
        # If the value is already in the set, a duplicate is found
        if value in unique_items:
            return True
        # Add the value to the set
        unique_items.add(value)
    
    # If no duplicates are found, return False
    return False

# Example usage
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))