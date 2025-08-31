class LinearSearch:
    """
    Linear Search Algorithm

    This function performs a linear search on a given list to find the index of a target element.

    Parameters:
    arr (list): The list to search through.
    target: The element to search for in the list.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """ 
    def linear_search(arr,target):

        for i in range(len(arr)):
            if arr[i] == target:    
                return i
        return -1   


# Example usage:
arr = [4, 2, 3, 5, 1]
target = 5
result = LinearSearch.linear_search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")