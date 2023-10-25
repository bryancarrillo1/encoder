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

def decoder(encode):
    string = ''
    encoded = str(encode)
    for i in encoded:
        if i == 0:
            string += 7
        if i == 1:
            string += 8
        if i == 2:
            string += 9
        else:
            temp = int(i)
            new = temp - 3
            newer = str(new)
            string += newer

    return string


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

        if option == 2:
            decoder(encoder())

        if option == 3:
            run = False


if __name__ == '__main__':
    main()
