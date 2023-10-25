def encoder():
    password = input("Enter a password to encode: ")
    string = ""

    for i in password:
        encoded = int(i) + 3

        if encoded == 10:
            encoded = 0

        if encoded == 11:
            encoded = 1

        if encoded == 12:
            encoded = 2

        string += str(encoded)

    return print(f'Your encoded password is {string}')


def main():
    run = True

    while run:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1: # need you to make encoder return its string into a variable that is re-callable
            encoder()

        # if option == 2:
        #     decoder()

        if option == 3:
            run = False



if __name__ == '__main__':
    main()
