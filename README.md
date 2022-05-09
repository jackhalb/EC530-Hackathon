# EC530-Hackathon

Code was inspired by this repository: https://github.com/engineer-man/youtube/tree/master/141

## Purpose

In this project, the goal is to write a peer-to-peer (P2P) messaging service between two clients to make a decentralized messaging application. The idea for the "hackathon" project is that this project can be used in a hackathon-style setting and is quite resistant to hacking (as it is P2P). There are two primary roles in this communication process, namely the client and the server. The server side connects to both clients and exchanges the IP addresses between the clients. This way, each client will know the IP it should be sending messages to. However, the server does not facilitate communication between the two clients, but only sets up the communication protocol. The client code communicates to the server at first to receive the IP of the other client and then attempts communication with the other client.

## How to use

To run the code, one will need three computers (either physical or virtual machines). On all three machines it is required that python three is installed so that the code can run. One computer will act as the server and the two machines engaging in chat will act as the client. On the computer you wish to run as the server, open a shell and navigate to the directory where the project is cloned to. After this, simply type "python3 server.py" (without quotes) and the server should begin running. Next, on the other two computers, navigate to the project directory in a shell and type "python3 client.py" (without quotes). When both clients have connected to the server, the server will then exchange IP addresses and then the two clients will connect to one another. Finally, you can begin messaging!

## Descriptions of Modules

### client.py
First, we define the server's IP and port for communication. This will be referred to as the "rendezvous" server. Next, we create a socket, bind to the localhost's internal IP and port and sends a single byte to the rendesvous server to let to server know it is ready to send it's IP. After this happens, we enter a while loop where we continuously receive from the rendesvous server. At this stage the server waits for the second client to connect and when "ready" is received the client knows that the server is ready and waiting for the other client. After this point, we then read from the server socket again, and this hangs because the server will not send another message to this client until it receives connection from the second client. After we receive this we punch a hole to the other client and create another socket to do this. We then send a byte to the client to establish connection. Finally, we create a new thread with the listen() function that will continuously listen for the other client while the console appication runs. In this way, one thread runs the bottom infinite while loop to send messages, and the newly created thread listens for messages from the other client.

### server.py
This module is a litte less complicated; it starts by binding to itself with a new socket, and listens in an infinite while loop for clients to connect. Similar to in client.py, Line 12 hangs until a transmission is received from a client, appends it to known clients, and sends ready to the client to let the client know to wait. Once the number of clients reaches 2, the while loop breaks and sends over the ports and IPs to the respective clients.

## Future Improvements

1. Create a frontend, either through a mobile application or a website.
2. Instead of having a rendesvous server, have a "signup" webpage as part of the frontend. When a user signs up, they can add their name and IP as part of their "account," and other users can add IPs of others via this service, i.e. make it more of a social network that is completely P2P besides exchanging IPs.
