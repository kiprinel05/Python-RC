import pygame
import random
import time
import math

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tema 2 - RC")
font = pygame.font.Font(None, 24)

# Colors
dark_bg = (20, 20, 30)
node_color = (255, 140, 0)
token_color = (50, 255, 50)
text_color = (255, 255, 255)
edge_color = (200, 200, 250)
shadow_color = (10, 10, 15)


def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


nodes = [f"C{i}" for i in range(10)]
ip_addresses = {node: generate_ip() for node in nodes}


class Token:
    def __init__(self, source, destination, message):
        self.source = source
        self.destination = destination
        self.message = message
        self.reached_destination = False
        self.history = []


def calculate_positions():
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    radius = 250
    positions = {}
    for i, node in enumerate(nodes):
        angle = (2 * math.pi * i) / len(nodes)
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        positions[node] = (x, y)
    return positions


positions = calculate_positions()


def draw_graph(token_position=None, source=None, destination=None, direction=1):
    screen.fill(dark_bg)

    for node, (x, y) in positions.items():
        pygame.draw.circle(screen, shadow_color, (x + 3, y + 3), 38)  # Shadow effect
        pygame.draw.circle(screen, node_color, (x, y), 35)
        ip_text = font.render(ip_addresses[node], True, text_color)
        text = font.render(node, True, text_color)
        screen.blit(ip_text, (x - ip_text.get_width() // 2, y - 70))
        screen.blit(text, (x - text.get_width() // 2, y - 10))

    for i in range(len(nodes)):
        pygame.draw.line(screen, edge_color, positions[nodes[i]], positions[nodes[(i + 1) % len(nodes)]], 2)

    if token_position:
        x, y = positions[token_position]
        pygame.draw.circle(screen, (34, 177, 76), (x, y), 42)  # Outer glow
        pygame.draw.circle(screen, token_color, (x, y), 40)
        text = font.render("Token", True, text_color)
        screen.blit(text, (x - text.get_width() // 2, y - 10))

    info_text = [
        f"Sursa: {source if source else '-'}",
        f"Dest: {destination if destination else '-'}",
        f"Locatie curenta: {token_position if token_position else '-'}",
        f"Sens: {'T' if direction == 1 else 'I.T.'}"
    ]
    for i, line in enumerate(info_text):
        text_surface = font.render(line, True, text_color)
        screen.blit(text_surface, (20, 20 + i * 25))

    pygame.display.flip()


def simulate_token_passing(last_position=None, direction=1):
    source, destination = random.sample(nodes, 2)
    token = Token(source, destination, "test message")
    current_position = nodes.index(last_position) if last_position else nodes.index(source)
    log_entries = [f"sursa: {source}, destinatia: {destination}\n"]

    while True:
        node = nodes[current_position]
        token.history.append(node)
        draw_graph(node, source, destination, direction)
        log_entries.append(f"{node}: muta jetonul")
        time.sleep(0.5)

        if node == destination:
            log_entries.append(f"{node}: am ajuns la destinatie")
            break

        current_position = (current_position + direction) % len(nodes)

    draw_graph()

    with open("result.txt", "a") as file:
        file.write("\n".join(log_entries) + "\n\n")

    return nodes[current_position]


def main():
    direction = 1
    last_position = None
    draw_graph(direction=direction)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    direction = 1
                elif event.key == pygame.K_2:
                    direction = -1
                elif event.key == pygame.K_SPACE:
                    last_position = simulate_token_passing(last_position, direction)

    pygame.quit()


main()
