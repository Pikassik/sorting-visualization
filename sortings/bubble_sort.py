from sortings import sorting


class BubbleSort(sorting.Sorting):
    def __init__(self, board):
        super().__init__(board)
        self.bubble_sort()
    
    def bubble_sort(self):
        for i in range(len(self.random_array)):
            for j in range(len(self.random_array) - 1):
                if (self.random_array[j] > self.random_array[j + 1] and
                        self.compare()):
                    self.swap(j, j + 1)
