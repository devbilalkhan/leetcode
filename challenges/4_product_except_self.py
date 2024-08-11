def productExceptSelf(nums):
    """
    Function to calculate the product of all elements in the array except the current
    element.
    
    :param nums: List of integers.
    :return: List of products such that each element at index i is the product of all 
    elements in the original array except nums[i].
    """
    
    # Initialize the output array with 1s
    output = [1] * len(nums)
    
    # Initialize prefix and suffix products
    prefix = 1
    suffix = 1
    
    # Calculate prefix products and store in output array
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply with the corresponding prefix product in
    # the output array
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    
    return output