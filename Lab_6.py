# Bryan Carrillo & Brando Santana


def encoder(password):

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

    return string

def decoder(encodedPassword):

    string = ""

    for i in encodedPassword:
        temp = int(i)

        if i == "2":
            num = 9
            new = str(num)
            string += new
        elif i == "1":
            num = 8
            new = str(num)
            string += new
        elif i == "0":
            num = 7
            new = str(num)
            string += new
        else:
            num = temp - 3
            new = str(num)
            string += new

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



        if option == 1:
            password = input("Enter a password to encode: ")

            encodedPassword = encoder(password)

            print("Your password has been encoded and stored!")

        if option == 2:
            decodedPassword = decoder(encodedPassword)

            print(f'The encoded password is {encodedPassword}, and the original password is {decodedPassword}.')

        if option == 3:
            run = False



if __name__ == '__main__':
    main()
