from socket import *
import time
import sys

def ping(host, port):
    resps = []

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)

    for seq in range(1,11):

        # Send ping message to server and wait for response back

        # On timeouts, you can use the following to add to resps
        # resps.append((seq, 'Request timed out', 0))

        # On successful responses, you should instead record the server
        # response and the RTT (must compute server_reply and rtt properly)

        # resps.append((seq, server_reply, rtt))

        # Fill in start

        # Record the time right before sending the ping
        send_time = time.time()

        # Create the ping message in the right format
        message = f"Ping {seq} {send_time}"

        # Send ping message to the server using UDP
        clientSocket.sendto(message.encode(), (host, port))

        # Wait for a response from the server
        try:
            response, serverAddress = clientSocket.recvfrom(1024)

            # record the time when the response is received
            receive_time = time.time()

            # convert the server response to string
            server_reply = response.decode()

            # calculate the round-trip time 
            rtt = receive_time - send_time

            # print server response
            print(server_reply)

            #print round-trip time
            print("RTT:", rtt)

            # save response, sequence number, and RTT
            resps.append((seq, server_reply, rtt))

        except timeout:

            #print timeout message if no response is received within 1 second
            print("Request timed out")

            # save timeout result with an RTT of 0
            resps.append((seq, 'Request timed out', 0))

        # Fill in end

    # Close the UDP socket after all 10 pings are complete
    clientSocket.close()

    return resps

if __name__ == '__main__':
    resps = ping('127.0.0.1', 12000)
    print(resps)