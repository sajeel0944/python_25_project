import socket
import threading

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))  # Replace "0.0.0.0" with your local IP if needed
server.listen(2)  # Allow 2 players

players = []
current_player = 0

def handle_client(conn, player_id):
    global current_player
    conn.send(str(player_id).encode())  # Tell the player their ID (0 or 1)
    
    while True:
        try:
            # Receive player position
            data = conn.recv(1024).decode()
            if not data:
                break
            
            # Send the other player's position
            other_player = 1 - player_id
            if len(players) > other_player:
                players[other_player].send(data.encode())
        except:
            break
    
    conn.close()
    players[player_id] = None

print("Server is running... Waiting for players")
while True:
    conn, addr = server.accept()
    print(f"Player {current_player} connected from {addr}")
    
    players.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, current_player))
    thread.start()
    current_player += 1