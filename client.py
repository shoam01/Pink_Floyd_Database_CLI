import socket

IP = "127.0.0.1"
PORT = 9

MAX_BITS = 12040

MENU = "1 - Get a list of all the albums\n2 - Get the songs in a given album\n3 - Get the length of a given song's name\n4 - Get a given song's lyrics\n5 - Get a given song's album\n6 - Get a list of songs with a given word in their name\n7 - Get a list of songs with a given word in their lyrics\n8 - Quit"

NOTHING = ""

QUIT = "Goodbye!"

OPTIONS = {"1" : "",
           "2" : "Enter an album: ",
           "3" : "Enter a song: ",
           "4" : "Enter a song: ",
           "5" : "Enter a song: ",
           "6" : "Enter a song's name: ",
           "7" : "Enter a lyric: ",
           "8" : ""}

ENTER_PASS = "Please enter the password: "
PASS_CORRECT = "The password is correct!"

def main() :
    with socket.socket() as sock :
        try :
            sock.connect((IP, PORT))

            print(sock.recv(MAX_BITS).decode())

        except Exception as e :
            print("Error: ", e)

        while True :
            try :
                password_msg = sock.recv(MAX_BITS).decode()
                print(password_msg)
            except Exception as e :
                print("Error: ", e)
                break

            if password_msg == ENTER_PASS :
                try :
                    password = input()
                    sock.sendall(password.encode())
                except Exception as e :
                    print("Error: ", e)
                    break

            elif password_msg == PASS_CORRECT :
                break

        while True :

            print(MENU)

            choice = input("Choose an option: ")

            data = ""

            try :
                if OPTIONS[choice] != NOTHING :
                    data = input(OPTIONS[choice])

            except Exception as e :
                print("Error: ", e)
                continue

            client_msg = f"{choice}&{data}"

            try :
                sock.sendall(client_msg.encode())

                response = sock.recv(MAX_BITS).decode()
                print(response)

                if response == QUIT :
                    break

            except Exception as e :
                print("Error: ", e)
                break


if __name__ == "__main__" :
    main()