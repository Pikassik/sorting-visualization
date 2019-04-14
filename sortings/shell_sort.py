from sortings import sorting


class ShellSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
    
    def sort(self):
        i = j = k = 0
        k = len(self.random_array) // 2
        while k > 0:
            i = k
            while i < len(self.random_array):
                t = self.random_array[i]
                j = i
                while j >= k:
                    if t < self.random_array[j - k]:
                        self.board.assign(j, self.random_array[j - k])
                    else:
                        break
                    j -= k
                self.board.assign(j, t)
                i += 1
            k //= 2
