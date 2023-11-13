### menu.py
# author - Thomas
# This class handles the menu parameters, allowing the program to be configured at startup
# The user can chose between using default settings or configuring every one themselves
# CONFIGURATION OPTIONS:
#   DISPLAY     - shows the live output frame in terminal
#   HSV_SLIDERS - (only if display is on) creates sliders allowing for live configuration of colour ranges
#   MODE        - 0 = run on PI. 1 = run on laptop. (changes the default hsv values accordingly)
#   SAVE        - save the output video (named 'output') in the file where the program was run



class MainMenu:

    # DEFAULT SETTINGS
    display = True
    hsv_sliders = False
    mode = False # laptop camera
    save = True
    morph = False

    def __init__(self):
        pass

    def main_menu(self):

        if (not self.take_input('Default_settings? y/n: ','y','n')):
            self.user_configure()

        return [self.display, self.hsv_sliders, self.mode, self.save, self.morph]


    # user_configure
    # This function allows the user to configure the program if default is unselected
    # It modifies the class variables to reflect user requirements
    def user_configure(self):

        self.display = self.take_input('show display? y/n: ','y','n')
        if self.display == True:
            self.hsv_sliders = self.take_input('colour sliders? y/n: ','y','n')
        self.mode = self.take_input('colour mode? laptop/pi: ','l','p')
        self.save = self.take_input('save video? y/n: ','y','n')
        self.morph = self.take_input('closed morphology? (improved cone detection, slower speed) y/n: ','y','n')


    # take_input
    # Asks for the user to input an option
    # Continues asking if user gets types an invalid string
    # More inputs could be added for more options
    # Inputs:
    #   display_string  - This is the display prompt the user is given
    #   a               - user input to return true
    #   b               - user input to return false
    # Output:
    #   true/false
    def take_input(self, display_string, a, b):

        while(1):
            key = input('{}'.format(display_string))

            if key == a:
                return True
            elif key == b:
                return False
            else:
                print("Summin wrong here. Try again homie...")