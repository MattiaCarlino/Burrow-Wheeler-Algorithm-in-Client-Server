
# Burrows-Wheeler Transform Client-Server System

## 📜 Description

This project implements a **client-server architecture** in Python for computing the **Burrows-Wheeler Transform (BWT)** of a string—an algorithm commonly used in data compression and bioinformatics. The client sends a string to the server, which processes it using the BWT algorithm and returns the result.

The implementation uses Python's built-in `socket` library for network communication.

## 📦 Project Structure

- `client.py` – Handles user input and communication with the server.
- `server.py` – Receives input from the client, computes the BWT, and returns the result.

## ⚙️ Requirements

- Python 3.x
- No external libraries required (only `socket`, included in Python's standard library)

## 🚀 Getting Started

1. **Clone or download** the repository to your machine.
2. First, run the **server**:

   ```bash
   python server.py
   ```

3. In a separate terminal, run the **client**:

   ```bash
   python client.py
   ```

4. Enter a lowercase-only string to transform. The server will return the BWT-encoded version.

## 🔍 Example Usage

```text
Communication with BWT server
Insert 'exit' for interrupt
Insert the string who you want convert
hello

The string sent by client: hello it length is: 5
The string after BWT conversion is: oellh it length is: 5
```

## 🧠 How the Burrows-Wheeler Transform Works

1. **Append a special character (`$`)** at the end of the input string.
2. **Generate all cyclic rotations** of the string.
3. **Sort the rotations** in lexicographical (alphabetical) order.
4. **Build the BWT string** by taking the last character of each sorted rotation.

Example with the string `"banana"`:

- Appended string: `banana$`
- Rotations: `banana$`, `anana$b`, ..., `$banana`
- Sorted: `$banana`, `a$banan`, ..., `nana$ba`
- BWT result: `annb$aa`

## 🛠️ Technical Details

### Communication

- TCP/IP protocol
- Message format: `"length:string"`
- Encoding: `utf-8`

### Input Validation (Client Side)

- Only lowercase letters (`a-z`) allowed
- Typing `exit` ends the session

### Error Handling

- Handles server unavailability (`ConnectionRefusedError`)
- Checks for invalid or empty messages

## 📈 Future Improvements

- Add **inverse BWT** functionality
- Save and display transformation statistics
- Implement a graphical user interface (GUI)
- Support strings with numbers or special characters

## 👨‍💻 Author

Mattia Carlino – 5FT-I – ITIS Archimede  
School Year: 2024/2025

## 📚 References

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Wikipedia – Burrows-Wheeler Transform](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform)
