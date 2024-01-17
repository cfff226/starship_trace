# A log management tool that reads shipping logs saved as text files
# And displays them to a user in a presentable and readable fashion

import pandas as pd


list_of_files = ["sep-23.txt", "oct-23.txt", "nov-23.txt", "dec-23.txt"]


# Add item to cart
def main():
    print(
        "----------------------------------------------------------------------------------\n\t\t\t\t\tMENU\n"
    )
    for i in range(len(list_of_files)):
        print(str(i + 1) + ". " + list_of_files[i])
    print(
        "\n----------------------------------------------------------------------------------\n"
    )
    try:
        choice = str(
            input("Please enter the name of the text file that you wish to view: \n")
        )
        if choice in list_of_files:
            # read text file into pandas DataFrame
            log_data = pd.read_table(choice, sep=";")
            print(f"\n{log_data}\n")

        else:
            print("\n\t\t\tYour choice has not been recognised\n")
            main()
    except ValueError:
        print("\n\t\t\tYou have entered an incorrect value\n")
        main()


main()
