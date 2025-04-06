import pygame
import socket

# Network setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5555))  # Replace "localhost" with server IP

# Game setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Player 2 (Arrow Keys)")

player_id = int(client.recv(1024).decode())  # Get player ID (0 or 1)
x, y = 100 if player_id == 0 else 700, 300
speed = 5

running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement (Arrow Keys for Player 2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: y -= speed
    if keys[pygame.K_DOWN]: y += speed
    if keys[pygame.K_LEFT]: x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    
    # Send position to server
    client.send(f"{x},{y}".encode())
    
    # Receive other player's position
    try:
        data = client.recv(1024).decode()
        if data:
            other_x, other_y = map(int, data.split(','))
            pygame.draw.rect(screen, (0, 255, 0), (other_x, other_y, 50, 50))  # Draw other player
    except:
        pass
    
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))  # Draw current player
    pygame.display.update()

client.close()
pygame.quit()