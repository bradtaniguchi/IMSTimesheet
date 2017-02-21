#!/usr/bin/python3

from tkinter import ttk
from tkinter import ttk
from app.Application import Application
from app.ioHandler import write_to_file
from app.ioHandler import read_config


def main():
    '''
    using ioHanlder, we need to read the config files, then pass them to the
    application root.
    '''
    users = read_config(verbose=True)
    root = Application(users=users)
    root.mainloop()


if __name__ == '__main__':
    main()

