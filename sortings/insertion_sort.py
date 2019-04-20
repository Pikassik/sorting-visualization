from sortings import sorting


class InsertionSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
    
    def sort(self):
        for i in range(1, len(self.random_array)):
            for j in range(i, 0, -1):
                self.board.update()
                if self.random_array[j] < self.random_array[j - 1]:
                    self.board.swap(j - 1, j)
                else:
                    self.board.update()
                    break
