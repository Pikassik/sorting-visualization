from sortings import sorting


class ShakerSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
        self.shaker_sort()

    def shaker_sort(self):
        left = 0
        right = len(self.random_array) - 1
        while left <= right:
            for i in range(left, right, +1):
                self.compare()
                if self.random_array[i] > self.random_array[i + 1]:
                    self.swap(i, i + 1)
            right -= 1
            for i in range(right, left, -1):
                self.compare()
                if self.random_array[i - 1] > self.random_array[i]:
                    self.swap(i, i - 1)
            left += 1
