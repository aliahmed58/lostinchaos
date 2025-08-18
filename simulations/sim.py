import pygame
import math

led_size = 32
light_white = (170, 170, 170)
red = (255, 0, 0)
H = 32
W = 24
radius = led_size // 2 - 2

buffer = [0] * (W * H)

# column major order
letters = {
    'a': [
        0b1111,
        0b1010,
        0b1010,
        0b1111
    ]
}

def printb(x):
    print("{:08b}".format(x))

def validate(x, y):
    return x < W and x >= 0 and y < H and y >= 0

def draw_letter(x, y, letter):
    if not validate(x, y) or not validate(x + 4, y + 4):
        return

    l_arr = letters[letter] 
    for c in range(4):
        rd = l_arr[c]
        for r in range(4):
            if rd & (0b1000 >> r):
                buffer[W * (r + y) + (c + x)] = 1


def draw_rect(x, y, w, h):
    if not validate(x, y) or not validate(x + w, y + h):
        return
    
    for c in range(x, x + w):
        for r in range(y, y + h):
            buffer[W * r + c] = 1


def render(screen):
    start_y_matrix = 0
    end_y_matrix = H // 8
    matrix_data = [0] * (end_y_matrix - start_y_matrix)
    for col in range(W):
        strip = col // 8
        for row in range(H):
            # only need to do this in python, not for arduino
            if buffer[W * row + col] == 0:
                cx = col * led_size + led_size // 2
                cy = row * led_size + led_size // 2
                pygame.draw.circle(screen, light_white, (cx, cy), radius)
                continue

            matrix = row // 8
            matrix_cell = row % 8
            matrix_data[matrix] |= int(math.ceil(pow(2, (7 - matrix_cell))))
        
        for m in range(end_y_matrix):
            write_to_nth_matrix(screen, strip, m, 8 - (col % 8), matrix_data[m])
            matrix_data[m] = 0


def draw_leds(screen):
    color = light_white
    for r in range(H):
        for c in range(W):
            cx = c * led_size + led_size // 2
            cy = r * led_size + led_size // 2
            pygame.draw.circle(screen, color, (cx, cy), radius)

def draw_grid_lines(screen):
    # Vertical lines every 8 columns
    for col in range(0, W, 8):
        x = col * led_size
        pygame.draw.line(screen, "red", (x, 0), (x, H * led_size), 2)
    # Horizontal lines every 8 rows
    for row in range(0, H, 8):
        y = row * led_size
        pygame.draw.line(screen, "red", (0, y), (W * led_size, y), 2)

def write_to_nth_matrix(screen, strip_no, matrix_no, d1, d2):
    cx = (strip_no * 8 * led_size) + (8 - d1) * led_size + led_size // 2
    start_y = matrix_no * led_size * 8
    for i in range(8):
        if d2 & 128:
            pygame.draw.circle(screen, "red", (cx, start_y + led_size * i + led_size // 2), radius)
        d2 = d2 << 1


def main():
    pygame.init()
    screen = pygame.display.set_mode((W * led_size, H * led_size))
    clock = pygame.time.Clock()
    running = True


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        draw_grid_lines(screen)
        render(screen)
        draw_letter(10, 7, 'a')
        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(20)  # limits FPS to 60

    pygame.quit()
    

main()

