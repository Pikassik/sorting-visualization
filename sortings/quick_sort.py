from sortings import sorting
import copy


class QuickSort(sorting.Sorting):
    def __init__(self, board):
        super().__init__(board)
        self.quick_sort(0, len(self.random_array) - 1)

    def quick_sort(self, first, last):
        if first < last:
            pivot_pos = self.partition(first, last)
            if pivot_pos > first:
                self.quick_sort(first, pivot_pos - 1)
            if pivot_pos + 1 <= last:
                self.quick_sort(pivot_pos + 1, last)

    def partition(self, first, last):
        if last == first:
            return first
        pivot = copy.copy(self.random_array[last])
        i = first
        j = last - 1
        while i <= j:
            while (self.random_array[i] < pivot and i < last and
                    self.compare()):
                i += 1
            while (self.random_array[j] >= pivot and j >= first and
                    self.compare()):
                j -= 1
            if i < j:
                self.swap(i, j)
                i += 1
                j -= 1
        self.swap(i, last)
        return i
