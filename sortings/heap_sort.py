from sortings import sorting


class HeapSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
        self.back = len(self.random_array) - 1
        self.heap_sort()

    def heap_sort(self):
        self.build_heap()
        for i in range(len(self.random_array)):
            self.swap(0, self.back)
            self.back -= 1
            self.sift_down(0)

    def build_heap(self):
        for i in range(len(self.random_array) // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        while True:
            biggest = i
            left = 2 * i + 1
            right = 2 * i + 2
            self.compare()
            if (left <= self.back and self.random_array[left] >
                    self.random_array[biggest]):
                biggest = left
            self.compare()
            if (right <= self.back and self.random_array[right] >
                    self.random_array[biggest]):
                biggest = right
            if biggest != i:
                self.swap(biggest, i)
                i = biggest
            else:
                break
