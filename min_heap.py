class MinHeap:
    def __init__(self):
        self.heap: list[int] = []

    def left_child(self, parent: int) -> int:
        return 2 * parent + 1

    def right_child(self, parent: int) -> int:
        return 2 * (parent + 1)

    def parent(self, child: int) -> int:
        return (child - 1) // 2

    def swap(self, heap_array: list, i: int, j: int) -> None:
        """In place swap of two array elements."""
        if i != j:
            temp = heap_array[i]
            heap_array[i] = heap_array[j]
            heap_array[j] = temp

    def add(self, value: int) -> None:
        """
        Adds value into heap
        """
        self.heap.append(value)
        cur = len(self.heap) - 1
        self.restore_after_insertion(cur)

    def remove(self) -> int:
        """
        Removes smallest value from the heap
        """
        if len(self.heap) == 0: 
            return None
        res = self.heap[0]
        self.heap[0] = self.heap[-1] # move last index to top of array
        self.heap.pop() # remove last index
        if self.heap: # check if elements still in heap
            self.restore_after_removal() # bubble new root down
        return res
    
    def restore_after_insertion(self, cur_index) -> None:
        """
        Restores heap after insertion
        """
        while cur_index > 0 and self.heap[self.parent(cur_index)] > self.heap[cur_index]:
            par = self.parent(cur_index)
            self.swap(self.heap, par, cur_index)
            cur_index = par

    def restore_after_removal(self) -> None:
        """
        Restores heap properly after removing peek 
        """
        i = 0
        heap_size = len(self.heap)
        while self.left_child(i) < heap_size:
            smallest = i
            left, right = self.left_child(i), self.right_child(i)
            if left < heap_size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < heap_size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                return
            self.swap(self.heap, i, smallest)
            i = smallest
            
            
    def number_of_elements(self) -> int:
        """
        returns number of elements in the heap
        """
        return len(self.heap)

    def peek(self) -> int | None:
        """
        Returns smallest element in the heap without removing it.
        """
        return self.heap[0] if self.heap else None