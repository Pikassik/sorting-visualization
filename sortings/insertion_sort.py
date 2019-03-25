from sortings import sorting


class InsertionSort(sorting.Sorting):
    def __init__(self, board):
        super().__init__(board)
        self.insertion_sort()
    
    def insertion_sort(self):
        for i in range(1, len(self.random_array)):
            for j in range(i, 0, -1):
                if self.random_array[j] < self.random_array[j - 1] \
                        and self.compare():
                    self.swap(j - 1, j)
                else:
                    self.parent.update()
                    break
