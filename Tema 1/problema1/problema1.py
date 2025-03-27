import pygame
import random
import time

def create_matrix(binary_str):
    rows = len(binary_str) // 7
    matrix = [list(binary_str[i * 7:(i + 1) * 7]) for i in range(rows)]
    return matrix

def add_parity_bits(matrix):
    rows = len(matrix)
    cols = 7

    for row in matrix:
        row.append(str(row.count('1') % 2))

    parity_col = []
    for col in range(cols + 1):
        ones_count = sum(1 for row in matrix if row[col] == '1')
        parity_col.append(str(ones_count % 2))

    matrix.append(parity_col)

def corrupt_bit(matrix):
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    rand_row, rand_col = random.randint(0, rows - 1), random.randint(0, cols - 1)
    matrix[rand_row][rand_col] = '1' if matrix[rand_row][rand_col] == '0' else '0'
    return rand_row, rand_col

def detect_error(matrix):
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    error_row, error_col = -1, -1

    for i in range(rows):
        if sum(1 for c in matrix[i][:cols] if c == '1') % 2 != int(matrix[i][cols]):
            error_row = i
            draw_matrix(screen, font, matrix, highlight=(i, -1), step=3, delay=1.0, message=f"Eroare detectata la randul {i + 1}")
            break

    for j in range(cols):
        if sum(1 for i in range(rows) if matrix[i][j] == '1') % 2 != int(matrix[rows][j]):
            error_col = j
            draw_matrix(screen, font, matrix, highlight=(-1, j), step=3, delay=1.0, message=f"Eroare detectata la col {j + 1}")
            break

    return error_row, error_col

def pulsate(screen, rect, delay=0.5, color=(0, 255, 0)):
    for _ in range(3):
        pygame.draw.rect(screen, color, rect, 2)
        pygame.display.flip()
        time.sleep(delay)
        pygame.draw.rect(screen, (50, 50, 50), rect, 2)
        pygame.display.flip()
        time.sleep(delay)

def draw_matrix(screen, font, matrix, highlight=None, step=0, delay=0, message=""):
    screen.fill((30, 30, 30))
    cell_size = 50
    margin = 10

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            rect = pygame.Rect(j * cell_size + margin, i * cell_size + margin, cell_size - 5, cell_size - 5)
            if step == 1 and (i, j) == highlight:
                color = (255, 0, 0)
                pulsate(screen, rect, color=(255, 0, 0))
            elif step == 2 and (i, j) == highlight:
                color = (0, 255, 0)
                pulsate(screen, rect, color=(0, 255, 0))
            elif step == 3 and (i == highlight[0] or j == highlight[1]):
                color = (0, 150, 255)
            else:
                color = (255, 255, 255)

            pygame.draw.rect(screen, (50, 50, 50), rect)
            text = font.render(cell, True, color)
            screen.blit(text, (rect.x + 15, rect.y + 10))

    text_surface = font.render(message, True, (255, 255, 255))
    screen.blit(text_surface, (10, 350))

    pygame.display.flip()
    time.sleep(delay)

def main():
    global screen, font

    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Biti de paritate bidimensionala")
    font = pygame.font.Font(None, 30)

    binary_str = "1111111"
    matrix = create_matrix(binary_str)
    add_parity_bits(matrix)

    running = True
    step = 0
    corrupted_pos = None
    detected_pos = None

    draw_matrix(screen, font, matrix, message="Corupe un bit - space")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if step == 0:
                        corrupted_pos = corrupt_bit(matrix)
                        draw_matrix(screen, font, matrix, corrupted_pos, step=1, delay=1.0, message="Bit corupt. Acum detecteaza-l - space")
                        step += 1
                    elif step == 1:
                        detected_pos = detect_error(matrix)
                        draw_matrix(screen, font, matrix, detected_pos, step=2, delay=1.0, message="Ai detectat eroarea - corecteaza - space")
                        step += 1
                    elif step == 2:
                        if detected_pos != (-1, -1):
                            row, col = detected_pos
                            matrix[row][col] = '1' if matrix[row][col] == '0' else '0'
                            draw_matrix(screen, font, matrix, detected_pos, step=3, delay=1.0, message="Ai corectat-o - restart? - space")
                        step += 1
                    else:
                        step = 0
                        matrix = create_matrix(binary_str)
                        add_parity_bits(matrix)
                        draw_matrix(screen, font, matrix, message="Corupe un bit - space")
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
