import pygame
import math

led_size = 22
light_white = (170, 170, 170)
red = (255, 0, 0)
H = 32
W = 24
radius = led_size // 2 - 2

px = 0
py = 0
pa = 2 * math.pi
pdx = pdy = 1
rad1 = 0.0174532925

led_array = [0] * (W * H)
for i in range(W):
    for j in range(H):
        if j == 0 or j == H - 1 or i == 0 or i == W - 1:
            led_array[W * j + i] = 1

led_array = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
]

def raycast(screen):
    global px, py, pa
    ra = pa - rad1 * 30
    ra = fix_angle(ra)
    for i in range(60):
        rx = ry = yo = xo = 0
        tan_a = -math.tan(ra)
        ra = fix_angle(ra)
        dof = 0

        # horizontal cast
        if ra > math.pi:
            ry = py * led_size - 0.0001
            rx = (((py * led_size) - ry) / tan_a) + px * led_size 
            yo = -led_size
            xo = -yo/tan_a
        if ra < math.pi:
            ry = py * led_size + led_size
            rx = (((py * led_size) - ry) / tan_a) + px * led_size
            yo = led_size
            xo = -yo/tan_a
        

        if ra == 0 or ra == math.pi:
            dof = 8
            rx = px * led_size
            ry = py * led_size

        mx = my = 0
        while dof < led_size:
            mx = int(rx // led_size)
            my = int(ry // led_size)
            index = W * my + mx
            if index >= 0 and index < W * H and led_array[index] == 1:
                break
            dof += 1
            rx += xo
            ry += yo
        
        hrx = rx
        hry = ry

        dof = 0
        # looking left
        if ra > (math.pi / 2) and ra < 3 * (math.pi / 2):
            rx = px * led_size - 0.0001
            ry = ((px * led_size) - rx) * tan_a + py * led_size
            xo = -led_size
            yo = -xo * tan_a
        if ra < (math.pi / 2) or ra > 3 * (math.pi / 2):
            rx = px * led_size + led_size
            ry = ((px * led_size) - rx) * tan_a + py * led_size
            xo = led_size
            yo = -xo * tan_a
        if ra == math.pi or ra == 0:
            rx = px
            ry = py
            dof = 8
        
        
        mx = my = 0
        while (dof < led_size):
            mx = int(rx // led_size)
            my = int(ry // led_size)
            index = W * my + mx
            if index < W * H and index >= 0 and led_array[index] == 1:
                break
            dof += 1
            rx += xo
            ry += yo

        disth = dist(hrx, hry, px * led_size, py * led_size)
        distv = dist(rx, ry, px * led_size, py * led_size)
        distT = min(disth, distv)

        cx = px * led_size + led_size // 2 
        cy = py * led_size + led_size // 2
        if (disth < distv):
            # pygame.draw.line(screen, "white", (cx, cy), (hrx, hry), 5)
            color = pygame.Color(150, 0, 0)
        else:
            color = pygame.Color(100, 0, 0)
            # pygame.draw.line(screen, "white", (cx, cy), (rx, ry), 5)

        distT = distT * math.cos(pa - ra)
        wall_height = (led_size / distT) * H * led_size * 4
        if wall_height > H * led_size * 4:
            wall_height = H * led_size * 2
        lO = (H * led_size / 2) - wall_height / 2
        # pygame.draw.line(screen, color, (i * 17, lO), (i * 17, lO + wall_height), 17)
        # draw as circles hehe
        start_y = int(round(lO / led_size)) * led_size
        end_y = int(round(lO + wall_height) / led_size) * led_size
        for j in range(start_y, end_y, led_size):
            cx = (i * led_size) + led_size // 2
            cy = j + led_size // 2
            pygame.draw.circle(screen, color, (cx, cy), radius)
        ra += rad1



def dist(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y2 - y1, 2))


def draw_player(screen):
    cx = px * led_size + led_size // 2
    cy = py * led_size + led_size // 2
    pygame.draw.circle(screen, red, (cx, cy), radius)

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

def draw_vector(screen):
    global px, py, pdx, pdy
    cx = px * led_size + led_size // 2
    cy = py * led_size + led_size // 2
    pygame.draw.line(screen, "yellow", (cx, cy), 
                     (cx + pdx * 100, cy + pdy * 100), 5)

def handle_key_press(keys):
    global px, py, pa ,pdy ,pdx
    if keys[pygame.K_a]:
        pa -= 0.1
        if pa < 0:
            pa += 2 * math.pi
        pdx = math.cos(pa) 
        pdy = math.sin(pa)
    if keys[pygame.K_d]:
        pa += 0.1
        if pa > 2 * math.pi:
            pa -= 2 * math.pi
        pdx = math.cos(pa)
        pdy = math.sin(pa)
    if keys[pygame.K_w]:
        py += round(pdy)
        px += round(pdx)
    if keys[pygame.K_s]:
        py -= round(pdy)
        px -= round(pdx)
    
def fix_angle(a):
    if a > 2 * math.pi:
        a -= 2 * math.pi
    if a < 0:
        a += 2 * math.pi
    return a

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
        keys = pygame.key.get_pressed()
        handle_key_press(keys)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        draw_leds(screen)
        # draw_grid_lines(screen)
        draw_player(screen)
        draw_vector(screen)
        raycast(screen)

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(20)  # limits FPS to 60

    pygame.quit()

main()