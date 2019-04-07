from sortings import sorting


class SelectionSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
        self.selection_sort()
    
    def selection_sort(self):
        for i in range(len(self.random_array)):
            minim = i
            for j in range(i, len(self.random_array)):
                self.compare()
                if self.random_array[j] < self.random_array[minim]:
                    minim = j
            self.swap(minim, i)
