class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        while i > 0 and self.heap[i][0] < self.heap[self._parent(i)][0]:
            parent_index = self._parent(i)
            self._swap(i, parent_index)
            i = parent_index

    def _heapify_down(self, i):
        n = len(self.heap)
        
        while True:
            left = self._left_child(i)
            right = self._right_child(i)
            smallest = i
            
            # Find the smallest among current node and its children, based on the value (index 0 of the tuple)
            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            
            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right
            
            # If the smallest is not the current node, swap and continue down
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Move the root element to the last position and pop it
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        
        # Restore heap property starting from the new root
        self._heapify_down(0)
            
        return min_val

def merge_k_lists(lists):
    min_heap = MinHeap()
    merged_list = []
    
    # Initialize the Min Heap with the first element from each list
    for i, lst in enumerate(lists):
        if lst:
            # Push a tuple: (value, list_index, element_index)
            # The Min Heap will compare based on the value (index 0)
            min_heap.push((lst[0], i, 0))
            
    # Extract the minimum element and push the next element from that list
    while min_heap.heap:
        # Get the smallest element available
        val, list_index, element_index = min_heap.pop()
        
        # Add the smallest element to the final merged list
        merged_list.append(val)
        
        # Check if there is a next element in the list from which we just pulled the value
        next_element_index = element_index + 1
        current_list = lists[list_index]
        
        if next_element_index < len(current_list):
            # Get the next value
            next_val = current_list[next_element_index]
            
            # Push the next element into the Min Heap
            min_heap.push((next_val, list_index, next_element_index))
            
    return merged_list

if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    
    print("Original lists:", lists)
    print("Merged and Sorted List:", merged_list)