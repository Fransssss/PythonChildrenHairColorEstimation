class Parents:

    # Black
    def black_black(self):
        print("There is a 100% change the first and second children would have black hair")

    def black_white(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have white, black, or gray hair")   # number formatting just to shorten the value

    def black_brown(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have brown, black, or chocolate hair")

    def black_blond(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have blond, black, or black-blonde hair")

    def black_red(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have red, black, or burgundy hair")

    def black_gray(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have gray, black, or dark-gray hair")

    # White
    def white_white(self):
        print("There is a 100% change the first and second children would have white hair")

    def white_brown(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have brown, white, or tan hair")

    def white_blond(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have blond, white, or towhead hair")

    def white_red(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have red, white, or pink hair")

    def white_gray(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have gray, white, or light-gray hair")

    # Brown
    def brown_brown(self):
        print("There is a 100% change the first and second children would have brown hair")

    def brown_blond(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have blond, brown, or bronde hair")

    def brown_red(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have red, brown, or maroon hair")

    def brown_gray(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have gray, brown, or purple hair")

    # Blond
    def blond_blond(self):
        print("There is a 100% change the first and second children would have blond hair")

    def blond_red(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have red, blond, or orange-red hair")

    def blond_gray(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have gray, blond, or silver-blonde hair")

    # Red
    def red_red(self):
        print("There is a 100% change the first and second children would have red hair")

    def red_gray(self):
        print("There is " + str(format(100/3, ".2f")) + "% the first and the second children have gray, red, or dull-red hair")

    # Gray
    def gray_gray(self):
        print("There is a 100% change the first and second children would have gray hair")


class Children(Parents):       # this has access to parents class
    pass
