from sortings import sorting


class GnomeSort(sorting.BaseSorting):
    def __init__(self, board):
        super().__init__(board)
        self.gnome_sort()

    def gnome_sort(self):
        i = 0
        while True:
            if i == len(self.random_array) - 1:
                break

            self.compare()
            if self.random_array[i] > self.random_array[i + 1]:
                self.swap(i, i + 1)
                if i != 0:
                    i -= 2
            i += 1
