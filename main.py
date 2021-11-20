import pygame
import sys
import math

def main():
    win = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    angle = 45
    depth = 5
    length = pygame.Vector2(0, -100)
    multiplier = 0.67

    while True:
        clock.tick(10)
        start_pos = pygame.Vector2(200, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    angle += 5
                if event.key == pygame.K_DOWN:
                    angle -= 5
                if event.key == pygame.K_RIGHT:
                    depth += 1
                if event.key == pygame.K_LEFT:
                    depth -= 1
                if event.key == pygame.K_w:
                    length.y += 5
                if event.key == pygame.K_s:
                    length.y -= 5
                if event.key == pygame.K_a:
                    multiplier += 0.05
                if event.key == pygame.K_d:
                    multiplier -= 0.05
        
        lines = tree(start_pos, length, angle, multiplier, depth)
        display(win, lines)

def display(win, lines):
    win.fill((0, 0, 0))
    for line in lines:
        pygame.draw.line(win, (255, 255, 255), line[0], line[1], 2)
    pygame.display.update()

def tree(start_pos, length, angle, multiplier, depth, lines=None):
    if lines is None:
        lines = []
    if depth <= 0:
        return

    options = (-angle*2, -angle, 0, angle, angle*2)

    new_pos = start_pos + length
    lines.append((start_pos, new_pos))
    temp_length = pygame.Vector2(length)
    temp_length.scale_to_length(temp_length.magnitude() * multiplier)
    for option in options:
        tree(new_pos, temp_length.rotate(option), angle, multiplier, depth-1, lines)
    
    return lines


if __name__ == "__main__":
    main()