from sortings import sorting


class BubbleSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
        self.bubble_sort()
    
    def bubble_sort(self):
        for i in range(len(self.random_array)):
            for j in range(len(self.random_array) - 1):
                self.compare()
                if self.random_array[j] > self.random_array[j + 1]:
                    self.swap(j, j + 1)
