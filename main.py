# Author: Fransiskus Agapa
# ========================================================================
# take input, which is the hair color or parents
# then the program would estimate the hair color of the first-two children
# there amount of hair color that people have is limited to about 6 color
# could be more but this program runs for general case only
# ======================================================================

from haircolor import Children

print("\n== Family Hair Color Traits ==")
print("1. Input parents' hair color")
print("2. Children's hair color estimation")
choice = input("choice: ")

children_hair_color = Children()   # has access to function in parents class
pa_hair_color = ""
ma_hair_color = ""
data_updated = 1                   # condition to make sure there is data - this has to be zero

while choice != 'e' and choice != 'E':
    if choice == '1':
        pa_hc = input("\nFather's hair color: ").lower()
        if pa_hc.isdigit():
            print("\n[ Invalid input - string only ]")
            print("[ Update Failed ]")

        else:
            ma_hc = input("Mother's hair color: ").lower()

            if ma_hc.isdigit():
                print("\n[ Invalid input - string only ]")
                print("[ Update Failed ]")

            else:
                pa_hair_color = pa_hc
                ma_hair_color = ma_hc
                if data_updated != 0:
                    data_updated -= 1
                print("[ Data Updated ]")

    elif choice == '2':
        print("\n[ Estimation Children Hair Color ]\n")
        if data_updated == 0:                      # if only data has been put / updated
            # Black
            if pa_hair_color == "black" and ma_hair_color == "black":
                children_hair_color.black_black()

            elif pa_hair_color == "black" and ma_hair_color == "white" or pa_hair_color == "white" and ma_hair_color == "black":
                children_hair_color.black_white()

            elif pa_hair_color == "black" and ma_hair_color == "brown" or pa_hair_color == "brown" and ma_hair_color == "black":
                children_hair_color.black_brown()

            elif pa_hair_color == "black" and ma_hair_color == "blond" or pa_hair_color == "blond" and ma_hair_color == "black":
                children_hair_color.black_blond()

            elif pa_hair_color == "black" and ma_hair_color == "red" or pa_hair_color == "red" and ma_hair_color == "black":
                children_hair_color.black_red()

            elif pa_hair_color == "black" and ma_hair_color == "gray" or pa_hair_color == "gray" and ma_hair_color == "black":
                children_hair_color.black_gray()

            # White
            elif pa_hair_color == "white" and ma_hair_color == "white":
                children_hair_color.white_white()

            elif pa_hair_color == "white" and ma_hair_color == "brown" or pa_hair_color == "brown" and ma_hair_color == "white":
                children_hair_color.white_brown()

            elif pa_hair_color == "white" and ma_hair_color == "blond" or pa_hair_color == "blond" and ma_hair_color == "white":
                children_hair_color.white_blond()

            elif pa_hair_color == "white" and ma_hair_color == "red" or pa_hair_color == "red" and ma_hair_color == "white":
                children_hair_color.white_red()

            elif pa_hair_color == "white" and ma_hair_color == "gray" or pa_hair_color == "gray" and ma_hair_color == "white":
                children_hair_color.white_gray()

            # brown
            elif pa_hair_color == "brown" and ma_hair_color == "brown":
                children_hair_color.brown_brown()

            elif pa_hair_color == "brown" and ma_hair_color == "blond" or pa_hair_color == "blond" and ma_hair_color == "brown":
                children_hair_color.brown_blond()

            elif pa_hair_color == "brown" and ma_hair_color == "red" or pa_hair_color == "red" and ma_hair_color == "brown":
                children_hair_color.brown_red()

            elif pa_hair_color == "brown" and ma_hair_color == "gray" or pa_hair_color == "gray" and ma_hair_color == "brown":
                children_hair_color.brown_gray()

            # blond
            elif pa_hair_color == "blond" and ma_hair_color == "blond":
                children_hair_color.blond_blond()

            elif pa_hair_color == "blond" and ma_hair_color == "red" or pa_hair_color == "red" and ma_hair_color == "blond":
                children_hair_color.blond_red()

            elif pa_hair_color == "blond" and ma_hair_color == "gray" or pa_hair_color == "gray" and ma_hair_color == "blond":
                children_hair_color.blond_gray()

            # red
            elif pa_hair_color == "red" and ma_hair_color == "red":
                children_hair_color.red_red()

            elif pa_hair_color == "red" and ma_hair_color == "gray" or pa_hair_color == "gray" and ma_hair_color == "red":
                children_hair_color.red_gray()

            # gray
            elif pa_hair_color == "gray" and ma_hair_color == "gray":
                children_hair_color.gray_gray()

            else:
                print("[ Color combination cannot be estimated ]")
        else:
            print("[ No Data ]")

    else:
        print("\n[ Invalid choice ]")

    print("\n== Family Hair Color Traits ==")
    print("1. Input parents hair color")
    print("2. Children's hair color estimation")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")