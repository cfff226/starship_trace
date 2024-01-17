# A log management tool that reads shipping logs saved as text files
# And displays them to a user in a presentable and readable fashion

list_of_files = ["sep-23.txt", "oct-23.txt", "nov-23.txt", "dec-23.txt"]

# Add item to cart
def main():
    print("----------------------------------------------------------------------------------\n\t\t\t\t\tMENU\n")
    for i in range(len(list_of_files)):
        print(str(i + 1) + ". " + list_of_files[i])
    print("\n----------------------------------------------------------------------------------\n")
    try:
        choice = str(input("Please enter the name of the text file that you wish to view: "))
        if choice not in list_of_files:
            print("Your choice has not been recognised")
            main()
    except ValueError:
        print("You have entered an incorrect value")
   
main()
