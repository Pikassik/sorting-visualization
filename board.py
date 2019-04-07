from tkinter import *
from time import sleep
import random
import sortings.bubble_sort
import sortings.insertion_sort
import sortings.gnome_sort
import sortings.heap_sort
import sortings.insertion_sort
import sortings.merge_sort
import sortings.quick_sort
import sortings.selection_sort
import sortings.shaker_sort
import sortings.shell_sort


class Board(Canvas):
    def __init__(self, parent, sort_type, width, height, arr_size):
        Canvas.__init__(self, parent, width=width, height=height,
                        background='black', highlightthickness=0)
        self.parent = parent
        self.sort_type = sort_type
        self.width = width
        self.height = height
        self.arr_size = arr_size
        self.gap = width / arr_size
        self.delay = self.parent.winfo_screenwidth() / self.arr_size
        self.random_array = [random.randint(1, self.height) for i in
                             range(self.arr_size)]
        self.columns = {}
        self.sortings = {
            "Bubble sort": sortings.bubble_sort.BubbleSort,
            "Insertion sort": sortings.insertion_sort.InsertionSort,
            "Shaker sort": sortings.shaker_sort.ShakerSort,
            "Gnome sort": sortings.gnome_sort.GnomeSort,
            "Selection sort": sortings.selection_sort.SelectionSort,
            "Shell sort": sortings.shell_sort.ShellSort,
            "Quick sort": sortings.quick_sort.QuickSort,
            "Heap sort": sortings.heap_sort.HeapSort,
            "Merge sort": sortings.merge_sort.MergeSort}
        self.init_board()

    def init_board(self):
        self.pack(side=TOP, expand=1, fill=BOTH)
        for i in range(0, self.arr_size):
            self.columns[i] = self.create_rectangle(self.gap * i,
                                                    self.height - (
                                                        self.random_array[i]),
                                                    self.gap * i + self.gap,
                                                    self.height, fill='white',
                                                    width=0)
        self.pack(side=TOP, expand=1, fill=BOTH)
        self.sortings[self.sort_type](self)
        sleep(2.)

    def swap(self, i, j):
        self.delete(self.columns[i])
        self.delete(self.columns[j])
        self.parent.update()
        self.random_array[i], self.random_array[j] = \
            self.random_array[j], self.random_array[i]
        self.columns[i] = self.create_rectangle(self.gap * i, self.height - (
            self.random_array[i]), self.gap * i + self.gap, self.height,
                                                fill='white', width=0)
        self.columns[j] = self.create_rectangle(self.gap * j, self.height - (
            self.random_array[j]), self.gap * j + self.gap, self.height,
                                                fill='white', width=0)
        self.parent.update()
        sleep(0.0005 * self.delay)

    def assignment(self, i, value):
        self.delete(self.columns[i])
        self.random_array[i] = value
        self.columns[i] = self.create_rectangle(self.gap * i,
                                                self.height -
                                                self.random_array[i],
                                                self.gap * i + self.gap,
                                                self.height, fill='white',
                                                width=0)
        self.parent.update()
        sleep(0.0005 * self.delay)

    def compare(self):
        self.parent.update()
        sleep(0.0001 * self.delay)
