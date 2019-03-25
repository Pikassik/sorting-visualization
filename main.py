import app
import tkinter

def main():
    root = tkinter.Tk()
    application = app.App(root)
    root.overrideredirect(True)
    root.mainloop()


if __name__ == '__main__':
    main()
