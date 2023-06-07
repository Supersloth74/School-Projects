"""

"""
import tkinter


class MPG_Calculator:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        # Create the top/middle/bottom frames for the Mpg program
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # Title label
        self.title_label = tkinter.Label(self.top_frame, text="Calculate Miles Per Gallon")
        # Create the labels for number of gallons the car holds, and number of miles it can
        # be driven on a full tank
        # and the display for mpg
        self.gallons_held_label = tkinter.Label(self.top_frame, text="Enter number of gallons the"
                                                                     " car can hold: ")
        self.miles_driven_label = tkinter.Label(self.middle_frame, text="Enter how many miles the car "
                                                                        "can be driven on a full tank: ")
        self.display_mpg_stringvar = tkinter.StringVar()
        self.display_mpg_label = tkinter.Label(self.bottom_frame, textvariable=self.display_mpg_stringvar)

        # Create the entry for gallons held, and miles can be driven
        self.gallons_held_entry = tkinter.Entry(self.top_frame, width=10)
        self.miles_drive_entry = tkinter.Entry(self.middle_frame, width=10)

        # Create the Calculate and Quit buttons
        self.calculate_mpg_button = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calculate_mpg)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the labels
        self.title_label.pack(side='top')
        self.gallons_held_label.pack(side='left')
        self.miles_driven_label.pack(side='left')
        self.display_mpg_label.pack(side='top')

        # Pack the entrys
        self.gallons_held_entry.pack(side='left')
        self.miles_drive_entry.pack(side='left')

        # Pack the buttons
        self.calculate_mpg_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack(side='top')
        self.middle_frame.pack(side='top')
        self.bottom_frame.pack(side='bottom')

        tkinter.mainloop()

    # Define the Calculate MPG function

    def calculate_mpg(self):
        miles = int(self.miles_drive_entry.get())
        gallons = int(self.gallons_held_entry.get())
        mpg = miles / gallons
        self.display_mpg_stringvar.set('Miles per gallon: ' + str(round(mpg, 2)))


mpg_gui = MPG_Calculator()
