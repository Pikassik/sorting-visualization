from board import *


class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title('Sorting Visualization')
        self.parent.geometry(
            '{}x{}+{}+{}'.format(self.parent.winfo_screenwidth(),
                                 self.parent.winfo_screenheight(), 0, 0))
        self.quit_button = None
        self.sort_button = None
        self.scale_arr_size = None
        self.select_sorting = None
        self.sortings = ["Bubble sort",
                         "Insertion sort",
                         "Shaker sort",
                         "Gnome sort",
                         "Selection sort",
                         "Shell sort",
                         "Quick sort",
                         "Heap sort",
                         "Merge sort"]
        self.selected_sorting = StringVar(parent)
        self.selected_sorting.set("Bubble sort")
        self.arr_size = IntVar()
        self.arr_size.set(20)
        self.set_ui()

    def on_scale(self, value):
        value = int(float(value))
        self.arr_size.set(value)

    def start_sorting(self):
        self.destroy_ui()
        try:
            board = Board(self.parent, self.selected_sorting.get(),
                          self.parent.winfo_screenwidth(),
                          self.parent.winfo_screenheight() - 75,
                          self.arr_size.get())
            board.destroy()
        except Exception as e:
            exit()
        self.set_ui()

    def destroy_ui(self):
        self.quit_button.destroy()
        self.sort_button.destroy()
        self.scale_arr_size.destroy()
        self.select_sorting.destroy()

    def set_ui(self):
        self.arr_size.set(20)
        self.pack(fill=BOTH, expand=1)
        self.quit_button = Button(self, text="Quit", command=self.quit)
        self.quit_button.place(x=5, y=10)
        self.sort_button = Button(self, text="Sort",
                                  command=self.start_sorting)
        self.sort_button.place(x=60, y=10)
        self.scale_arr_size = Scale(self, from_=20,
                                    to=self.parent.winfo_screenwidth(),
                                    resolution=20, command=self.on_scale,
                                    orient=HORIZONTAL)
        self.scale_arr_size.pack(anchor=NW, padx=200)
        self.select_sorting = OptionMenu(self, self.selected_sorting,
                                         *self.sortings)
        self.select_sorting.pack(anchor=NW)
