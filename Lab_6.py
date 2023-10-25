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

def decoder(encoded_password):
    pass


def main():
    run = True

    while run:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1: # I need encoder to return its string and then save it to a variable I can refer to.
            encoder()

        #if option == 2:
           #pass

        if option == 3:
            run = False


if __name__ == '__main__':
    main()
