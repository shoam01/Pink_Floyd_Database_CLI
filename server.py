import socket
import data
import hashlib

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9

MAX_BITS = 12040

MSG_SEP = "&"
CHOICE_POS = 0
DATA_POS = 1

SONGS, ALBUMS = data.parse_db()

PASS = hashlib.md5(b"nani").hexdigest()

def main() :
    with socket.socket() as listening_sock :
        listening_sock.bind((SERVER_IP, SERVER_PORT))
        listening_sock.listen(1)

        while True :
            client_sock, client_address = listening_sock.accept()

            try :
                client_sock.sendall(b"Welcome!")  # welcome message

                password = b""

                while hashlib.md5(password).hexdigest() != PASS :
                    client_sock.sendall(b"Please enter the password: ")
                    password = client_sock.recv(MAX_BITS)

                client_sock.sendall(b"The password is correct!")
            except Exception as e :
                print("Error: ", e)

            while True :
                try :
                    client_msg = client_sock.recv(MAX_BITS).decode().split(MSG_SEP)

                except Exception as e :
                    print("Error: ", e)
                    break

                try :
                    response = data.OPTIONS[client_msg[CHOICE_POS]](SONGS, ALBUMS, client_msg[DATA_POS])

                except Exception as e :
                    response = f"Error: {e}"

                try :
                    client_sock.sendall(response.encode())

                    if response == data.QUIT :
                        break

                except Exception as e :
                    print("Error: ", e)
                    break

            client_sock.close()


if __name__ == "__main__" :
    main()