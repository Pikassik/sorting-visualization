from sortings import sorting


class BubbleSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
    
    def sort(self):
        for i in range(len(self.random_array)):
            for j in range(len(self.random_array) - 1):
                self.board.update()
                if self.random_array[j] > self.random_array[j + 1]:
                    self.board.swap(j, j + 1)
