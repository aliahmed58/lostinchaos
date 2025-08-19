import pygame

# character designer to get the the pixels in the format
# 0b1111 where each binary value tells rows of a specific column
# variable size

# 5x5 sprites
DIM_X = 4
DIM_Y = 5
# scale factor to view it visibly
SCALE = 32
W = 32 * SCALE
H = 30 * SCALE

buffer = [0] * ((W // SCALE) * (H // SCALE))

def buffer2binary():
    output = {}
    cols = W // SCALE
    rows = H // SCALE
    blocks_x = cols // DIM_X
    blocks_y = rows // DIM_Y
    
    for x in range(blocks_x):
        for y in range(blocks_y):
            key = (x, y)
            block_cols = []
            for cx in range(DIM_X):
                val = 0 
                for cy in range(DIM_Y):
                    bx = x * DIM_X + cx
                    by = y * DIM_Y + cy
                    bit = buffer[by * cols + bx]
                    val = (val << 1) | bit
                block_cols.append(val)
            output[key] = block_cols
    return output

def draw_buffer(screen): 
    for i in range(W // SCALE):
        for j in range(H // SCALE):
            if buffer[SCALE * j + i]:
                pygame.draw.rect(screen, (64, 64, 64), (i * SCALE, j * SCALE, SCALE, SCALE))


def draw_grid(screen):
    for i in range(0, W, SCALE):
        pygame.draw.line(screen, "white", (i, 0), (i, H))
    for j in range(0, H, SCALE):
        pygame.draw.line(screen, "white", (0, j), (W, j))
    
def draw_seperators(screen):
    for i in range(0, W, SCALE * DIM_X):
        pygame.draw.line(screen, "red", (i, 0), (i, H))
    for j in range(0, H, SCALE * DIM_Y):
        pygame.draw.line(screen, "red", (0, j), (W, j))

def get_mouse_grid_coord(x, y):
    grid_x = int(x - x % SCALE)
    grid_y = int(y - y % SCALE)
    return (grid_x, grid_y)

def hover_mouse(screen, x, y):
    grid_x, grid_y = get_mouse_grid_coord(x, y)
    pygame.draw.rect(screen, "gray", (grid_x, grid_y, SCALE, SCALE))

def handle_mouse_event(x, y, mouse_btns):
    grid_x, grid_y = get_mouse_grid_coord(x, y)
    buffer_x = grid_x // SCALE
    buffer_y = grid_y // SCALE
    if mouse_btns[0]: 
        buffer[buffer_y * (W // SCALE) + buffer_x] = 1
    if mouse_btns[2]:
        buffer[buffer_y * (W // SCALE) + buffer_x] = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        mouse_btns = pygame.mouse.get_pressed()
        handle_mouse_event(*pygame.mouse.get_pos(), mouse_btns)

        screen.fill("black")
        hover_mouse(screen, *pygame.mouse.get_pos())
        draw_buffer(screen)
        draw_grid(screen)
        draw_seperators(screen)

        pygame.display.flip()

        clock.tick(20)  # limits FPS to 60

    pygame.quit()

main()

# output buffer as the format i need
output = buffer2binary()
formatted_list = []
for key, value in output.items():
    if sum(value) > 0:
        binary = "_".join(format(x, f"0{DIM_Y}b") for x in value)
        formatted_list.append(binary)

# pretty print lmao
print('[')
for i in formatted_list:
    print(f'\t0b{i}', end=", ")
    print()
print(']')