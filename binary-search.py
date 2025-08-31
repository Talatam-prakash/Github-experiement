class BinarySearch:
    """
    Perform binary search on a sorted array to find the index of the target element.    
    Parameters:
    arr (list): A sorted list of elements to search through.
    target: The element to search for in the list.
    Returns:

    int: The index of the target element if found, otherwise -1.
    Example:
    >>> arr = [1,10,22,34,46,50]
    >>> target = 5
    >>> BinarySearch.binary_search(arr, target)
    """ 
    
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2        
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    
        return -1

# Example usage:
arr = [1,10,22,34,46,50]
target = 50
result = BinarySearch.binary_search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")

