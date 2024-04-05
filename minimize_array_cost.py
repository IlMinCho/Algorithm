def getMinimumCost(arr):
    # Function to calculate the cost of two adjacent numbers with a potential number inserted.
    def cost_with_insert(a, b, num):
        return (num - a)**2 + (b - num)**2

    # Calculate the initial cost of the array.
    initial_cost = sum((arr[i] - arr[i-1]) ** 2 for i in range(1, len(arr)))

    # Find the maximum decrease in cost by inserting an element.
    max_decrease = 0
    for i in range(1, len(arr)):
        left = arr[i - 1]
        right = arr[i]
        # The optimal number to insert is the average of the two adjacent numbers,
        # but since we want an integer, we try both the floor and the ceil of the average.
        for num in [left, (left + right) // 2, (left + right + 1) // 2, right]:
            # Calculate the potential decrease in cost for this insertion.
            decrease = (left - right) ** 2 - cost_with_insert(left, right, num)
            # Update the maximum decrease.
            max_decrease = max(max_decrease, decrease)

    # The minimum cost is the initial cost minus the maximum decrease found.
    return initial_cost - max_decrease