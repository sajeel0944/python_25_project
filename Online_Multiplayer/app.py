import pygame
import socket
import threading
import pickle
import sys

# Game settings
WIDTH, HEIGHT = 500, 500
FPS = 60

# Network settings
HOST = 'localhost'
PORT = 5555

# Player colors and size
PLAYER_SIZE = 50
COLORS = [(0, 0, 255), (255, 0, 0)]

# Networking functions
def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Waiting for a player to join...")
    conn, addr = server.accept()
    print("Player connected from", addr)
    return conn

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    return client

# Thread to receive position from network
def receive_data(sock, player_rect):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            pos = pickle.loads(data)
            player_rect.x, player_rect.y = pos
        except:
            break

# Main game function
def main(is_server):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Multiplayer Game")
    clock = pygame.time.Clock()

    # Initial positions
    rects = [pygame.Rect(100, 100, PLAYER_SIZE, PLAYER_SIZE),
             pygame.Rect(300, 300, PLAYER_SIZE, PLAYER_SIZE)]

    # Networking setup
    sock = create_server() if is_server else connect_to_server()
    player_id = 0 if is_server else 1
    threading.Thread(target=receive_data, args=(sock, rects[1 - player_id]), daemon=True).start()

    # Game loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sock.close()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rects[player_id].x -= 5
        if keys[pygame.K_RIGHT]:
            rects[player_id].x += 5
        if keys[pygame.K_UP]:
            rects[player_id].y -= 5
        if keys[pygame.K_DOWN]:
            rects[player_id].y += 5

        # Send current player position
        try:
            sock.send(pickle.dumps((rects[player_id].x, rects[player_id].y)))
        except:
            pass

        # Draw
        win.fill((30, 30, 30))
        pygame.draw.rect(win, COLORS[player_id], rects[player_id])
        pygame.draw.rect(win, COLORS[1 - player_id], rects[1 - player_id])
        pygame.display.update()

if __name__ == "__main__":
    choice = input("Host or Join? (h/j): ").lower()
    is_server = choice == 'h'
    main(is_server)
