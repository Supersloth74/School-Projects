"""
Programmer: Madison McCurry
Assignment: Module 14 - Assignment 14
Date Completed: 11/25/21
Course: CITC 2391 - C02
Instructor: Martin Bell
"""
import tkinter


class tn_flag_gui:
    def __init__(self):
        # Main window (root) ####################################
        self.main_window = tkinter.Tk()

        # Canvas ####################################
        self.flag_canvas = tkinter.Canvas(self.main_window, height=300, width=500, bg='#BA0101')

        # Circles ####################################
        # White outer
        self.flag_canvas.create_oval(160, 60,
                                     325, 230,
                                     fill='#FFFFFF',
                                     outline='#FFFFFF')
        # Blue inner
        self.flag_canvas.create_oval(165, 65,
                                     320, 225,
                                     fill='#003366',
                                     outline='#003366')

        # Stars ####################################
        """self.flag_canvas.create_polygon(50, 25,
                                        70, 100,
                                        30, 45,
                                        80, 45,
                                        35, 100,
                                        fill='#FFFFFF') 
        """
        self.flag_canvas.create_polygon(10, 40,
                                        40, 40,
                                        50, 10,
                                        60, 40,
                                        90, 40,
                                        65, 60,
                                        75, 90,
                                        50, 70,
                                        25, 90,
                                        35, 60,
                                        fill='#FFFFFF')
        # Rectangles ####################################
        # Blue end one
        self.flag_canvas.create_rectangle(470, 300,
                                          500, 0,
                                          fill='#003366')
        # White end one
        self.flag_canvas.create_rectangle(465, 300,
                                          470, 0,
                                          fill='#FFFFFF',
                                          outline='#FFFFFF')

        # Pack ####################################
        self.flag_canvas.pack()

        # Main loop  ####################################
        tkinter.mainloop()


my_gui = tn_flag_gui()
