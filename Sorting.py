def bubble_sort(data):
  """
  Sorts a list of data using the Bubble Sort algorithm.

  Args:
      data (list): The list of data to be sorted.

  Returns:
      list: The sorted list.
  """
  n = len(data)
  swapped = False
  # Iterate through all elements
  for i in range(n-1):
    # Inner loop to compare adjacent elements
    for j in range(0, n-i-1):
      # Swap elements if they are in the wrong order
      if data[j] > data[j + 1]:
        data[j], data[j + 1] = data[j + 1], data[j]
        swapped = True
    # If no swaps occurred in the inner loop, the list is already sorted
    
  return data

def merge_sort(data):
  """
  Sorts a list of data using the Merge Sort algorithm (recursive).

  Args:
      data (list): The list of data to be sorted.

  Returns:
      list: The sorted list.
  """
  if len(data) <= 1:
    return data
  # Divide the list into two halves
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])

  # Merge the sorted halves
  merged = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  # Append remaining elements
  merged += left[i:]
  merged += right[j:]
  return merged

def quicksort(data, low, high):
  """
  Sorts a list of data using the Quick Sort algorithm (recursive).

  Args:
      data (list): The list of data to be sorted.
      low (int): The starting index of the sublist to sort.
      high (int): The ending index of the sublist to sort.

  Returns:
      None (sorts the data in-place).
  """
  if low < high:
    # Partition the list
    pivot_index = partition(data, low, high)
    # Recursively sort the sublists before and after the pivot
    quicksort(data, low, pivot_index - 1)
    quicksort(data, pivot_index + 1, high)

def partition(data, low, high):
   
  pivot = data[high]
  i = low - 1
  for j in range(low, high):
    if data[j] <= pivot:
      i += 1
      data[i], data[j] = data[j], data[i]
  data[i + 1], data[high] = data[high], data[i + 1]
  return i + 1

# Example usage
unsorted_data = [64, 34, 25, 12, 22, 11, 90]

print("Bubble Sort:")
sorted_data = bubble_sort(unsorted_data.copy())
print(sorted_data)

print("\nMerge Sort:")
sorted_data = merge_sort(unsorted_data.copy())
print(sorted_data)

print("\nQuick Sort:")
unsorted_data_copy = unsorted_data.copy()
quicksort(unsorted_data_copy, 0, len(unsorted_data_copy) - 1)
print(unsorted_data_copy)
