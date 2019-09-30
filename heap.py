# This is a sandbox to experiment with CoderPad's execution capabilities.
# It's a temporary, throw-away session only visible to you.

class MinHeap:
    def __init__(self, max_size):
        self.heap = [None] * max_size
        self.size = 0
        self.maxsize = max_size
        self.front = 1
    
    def get_parent(self, index):
        return index/2
    
    def left_child(self, index):
        return index*2
    
    def right_child(self, index):
        return index*2+1
    
    def is_leaf(self, index):
        print("index: {} size: {}".format(index, self.size))
        if index >= self.size/2 and index <= self.size:
            return True
        else:
            return False
    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
    
    def minHeapfy(self, index):
        print("heapfying: {} - {}".format(index, self.heap))
        if not self.is_leaf(index):
            if self.heap[index] > self.heap[self.left_child(index)] or \
                self.heap[index] > self.heap[self.right_child(index)]:
                    if self.heap[index] > self.heap[self.left_child(index)]:
                        self.swap(index, self.left_child(index))
                        self.minHeapfy(self.left_child(index))
                    else:
                        self.swap(index, self.right_child(index))
                        self.minHeapfy(self.right_child(index))
    def insert(self, value):
        if self.size > self.maxsize:
            raise ("Error");
        # Add in the last position
        self.size += 1
        self.heap[self.size] = value
        current = self.size
        while self.heap[current] < self.heap[self.get_parent(current)]:
            print("Swap: {} {}".format(self.heap[current], self.heap[self.get_parent(current)]))
            self.swap(current, self.get_parent(current))
            current = self.get_parent(current)
    def print_heap(self):
        index = 1
        while index <= self.size/2: 
            print("Parent: {}\n\
            \tLeft Child: {}\n\
            \tRight Child:{}".format(
                self.heap[index], 
                self.heap[self.left_child(index)],
                self.heap[self.right_child(index)])
                 )
            index += 1
    def remove(self):
        if self.size > 0:    
            element = self.heap[self.front]
            self.heap[self.front] = self.heap[self.size]
            self.size -= 1
            self.minHeapfy(self.front)
            print("Removed: {}".format(element))
            return element
        else:
            return None

if __name__ == "__main__":
    heap = MinHeap(20)
    heap.insert(10)
    heap.insert(7)
    heap.insert(1)
    heap.insert(2)
    heap.insert(20)
    heap.insert(5)
    heap.remove()
    heap.print_heap()
