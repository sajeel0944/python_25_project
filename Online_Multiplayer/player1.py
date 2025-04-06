import pygame
import socket

# Network setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))  # Replace "localhost" with server IP

# Game setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Player 1 (WASD)")

player_id = int(client.recv(1024).decode())  # Get player ID (0 or 1)
x, y = 100 if player_id == 0 else 700, 300
speed = 5

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement (WASD for Player 1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: y -= speed
    if keys[pygame.K_s]: y += speed
    if keys[pygame.K_a]: x -= speed
    if keys[pygame.K_d]: x += speed
    
    # Send position to server
    client.send(f"{x},{y}".encode())
    
    # Receive other player's position
    try:
        data = client.recv(1024).decode()
        if data:
            other_x, other_y = map(int, data.split(','))
            pygame.draw.rect(screen, (255, 0, 0), (other_x, other_y, 50, 50))  # Draw other player
    except:
        pass
    
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))  # Draw current player
    pygame.display.update()

client.close()
pygame.quit()