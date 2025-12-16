import heapq
import time

def min_cost_to_join_cables(cable_lengths):
    """
    Calculates the minimum cost required to join all network cables using a min-heap.
    
    The greedy strategy is applied: always join the two shortest cables available.
    
    :param cable_lengths: A list of integers representing the lengths of the initial cables.
    :return: An integer representing the minimum total cost of joining.
    """
    if len(cable_lengths) <= 1:
        return 0

    # Convert the list of lengths into a min-heap in place
    heapq.heapify(cable_lengths)

    total_cost = 0

    # Continue joining until only one cable (the final merged cable) remains in the heap
    while len(cable_lengths) > 1:
        
        # Extract the two shortest cables (minimum elements)
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        
        # Calculate the cost of the current join (sum of their lengths)
        current_join_cost = shortest1 + shortest2
        
        # Add the current cost to the overall total cost
        total_cost += current_join_cost
        
        # Insert the new, merged cable back into the heap
        heapq.heappush(cable_lengths, current_join_cost)

    return total_cost

if __name__ == "__main__":
    
    # Basic case
    cables_a = [4, 3, 2, 6]
    start_time_a = time.perf_counter()
    cost_a = min_cost_to_join_cables(cables_a.copy())
    end_time_a = time.perf_counter()
    
    print(f"Initial Cable Lengths: {cables_a}")
    print(f"Minimum Total Cost: {cost_a}")
    print(f"Execution Time: {end_time_a - start_time_a:.6f} seconds")
    print("-" * 30)

    # Larger list
    cables_b = [10, 20, 5, 15, 30, 25]
    start_time_b = time.perf_counter()
    cost_b = min_cost_to_join_cables(cables_b.copy())
    end_time_b = time.perf_counter()
    
    print(f"Initial Cable Lengths: {cables_b}")
    print(f"Minimum Total Cost: {cost_b}")
    print(f"Execution Time: {end_time_b - start_time_b:.6f} seconds")
    print("-" * 30)

    # Edge case (single cable)
    cables_c = [100]
    cost_c = min_cost_to_join_cables(cables_c.copy())
    print(f"Initial Cable Lengths: {cables_c}")
    print(f"Minimum Total Cost: {cost_c}")