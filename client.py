import socket as s

HOST = "127.0.0.1"
PORT = 12345

def input_validation_message(message):

    message = message.lower()
    for i in range(0,len(message)):
        if(ord(message[i]) < 97 or ord(message[i]) > 123):
            return False

    return True

def start_client():

    try:

        with s.socket(s.AF_INET,s.SOCK_STREAM) as socket_client:
            socket_client.connect((HOST,PORT))
            while True:
                print("Communication with BWT server")
                print("Insert 'exit' for interrupt")
                messaggio = input("Insert the string who you want convert" + "\n")
                
                if(messaggio.lower() == 'exit'):
                    print("You're exit from communication")
                    break

                if(input_validation_message(message)):
                    len_string = len(message)
                    print(f"The string sent by client: {message} it length is: {len_string}")
                    message = str(len_string) + ":" + message
                    socket_client.sendall(message.encode('utf-8'))
                    message_for_server = socket_client.recv(1024)
                    message_for_server_split = message_for_server.decode().split(":")
                    print(f"The string after BWT conversion is: {message_for_server_split[1]} it length is: {message_for_server_split[0]}")

    except ConnectionRefusedError:
        print("Problem with server connection")

if(__name__ == "__main__"):

    start_client()