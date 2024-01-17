# A log management tool that reads shipping logs saved as text files
# And displays them to a user in a presentable and readable fashion

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
        with open(str(choice), "r") as log_file:
            log_data = log_file.read().split("\n")
            print(log_data)
        if choice not in list_of_files:
            print("\n\t\t\tYour choice has not been recognised\n")
            main()
    except ValueError:
        print("\n\t\t\tYou have entered an incorrect value\n")
        main()


main()
