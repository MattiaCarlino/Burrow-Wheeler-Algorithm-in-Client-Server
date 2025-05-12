import socket as s

HOST = "127.0.0.1"
PORT = 12345

def str_to_BWT(client_message,len_string):
    permutations_string = {
        0: client_message +"$"
    }
    
    print("Calculation of all permutation of the string: ")
    print(f"permutation {0}: {permutations_string[0]}")
    for i in range(0,len(client_message)):
        part_before_dollar = client_message[slice(i+1)]
        part_past_dollar = client_message[slice(i+1,len_string)]
        permutations_string[i+1] = part_before_dollar + "$"+ part_past_dollar
        print(f"permutation {i+1}: {permutations_string[i+1]}")

    order_permutations_string = dict(sorted(permutations_string.items(), key=lambda item: item[1]))
    final_string = ""
    print("Permutation order by alphabetic order: ")
    for permutation in order_permutations_string.values():
        count = 0
        print(f"permutation {count}: {permutation}")
        final_string = final_string + permutation[len_string]
        count = count +1
    
    print("we take each final letter of the permutations, following the ordering just done")
    print(f"string convert in BWT is: {final_string}")
    return final_string
    

def start_server():
    with s.socket(s.AF_INET, s.SOCK_STREAM) as socket_server:
        socket_server.bind((HOST, PORT))
        socket_server.listen(1)

        try:
            while True:
                conn, addr = socket_server.accept()
                print("The client is connect to the server")
                with conn:
                    while True:
                        message_client = conn.recv(1024)
                        message_client = message_client.decode('utf-8')
                        string_split = message_client.split(":")
                        print(f"The server received: {string_split[1]} with length: {string_split[0]}")
                        if not message_client:
                            break
                        message_BWT = str_to_BWT(string_split[1],int(string_split[0]))
                        final_message = str(len(message_BWT)) + ":" + message_BWT
                        conn.sendall(final_message.encode('utf-8'))
        except Exception as e:
            print(e)
        except ConnectionAbortedError:
            print("Problem with connection")
        
if(__name__ == "__main__"):
    
    start_server()