from sortings import sorting


class MergeSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)

    def sort(self):
        self.merge_sort(0, len(self.random_array))

    def merge_sort(self, first, last):
        if (last - first <= 1):
            return
        border = (last - first) // 2 + first
        self.merge_sort(first, border)
        self.merge_sort(border, last)
        merged = self.merge(border, first, last)
        for i in range(first, last):
            self.board.assign(i, merged[i - first])

    def merge(self, border, first, last):
        merged = [0 for i in range(last - first)]
        i = j = 0
        while (i < border - first and j < last - border):
            self.board.update()
            if self.random_array[first + i] <= self.random_array[border + j]:
                merged[i + j] = self.random_array[first + i]
                i += 1
            else:
                merged[i + j] = self.random_array[border + j]
                j += 1
        if first + i == border:
            while border + j < last:
                merged[i + j] = self.random_array[border + j]
                j += 1
        else:
            while first + i < border:
                merged[i + j] = self.random_array[first + i]
                i += 1
        return merged
