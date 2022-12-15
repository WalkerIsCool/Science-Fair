points=[(1, 19,0), (1, 19, 1), (1, 19, 2), (1, 19, 3), (1, 18, 8), (1, 18, 13), (3, 18, 18), (3, 18, 19), (3, 18, 20), (3, 18, 21), (3, 17, 26), (3, 17, 31), (1, 17, 36), (1, 17, 37), (1, 17, 38), (1, 17, 39), (1, 16, 44), (1, 16, 49), (3, 16, 54), (3, 16, 55), (3, 16, 56), (3, 16, 57), (3, 15, 62), (3, 15, 67), (1, 15, 72), (1, 15, 73), (1, 15, 74), (1, 15, 75), (1, 14, 80), (1, 14, 85), (3, 14, 90), (3, 14, 91), (3, 14, 92), (3, 14, 93), (3, 13, 98), (3, 13, 103), (1, 13, 108), (1, 13, 109), (1, 13, 110), (1, 13, 111), (1, 12, 116), (1, 12, 121), (3, 12, 126), (3, 12, 127), (3, 12, 128), (3, 12, 129), (3, 11, 134), (3, 11, 139), (1, 11, 144), (1, 11, 145), (1, 11, 146), (1, 11, 147), (1, 10, 152), (1, 10, 157), (3, 10, 162), (3, 10, 163), (3, 10, 164), (3, 10, 165), (3, 9, 170), (3, 9, 175), (1, 9, 180), (1, 9, 181), (1, 9, 182), (1, 9, 183), (1, 8, 188), (1, 8, 193), (3, 8, 198), (3, 8, 199), (3, 8, 200), (3, 8, 201), (3, 7, 206), (3, 7, 211), (1, 7, 216), (1, 7, 217), (1, 7, 218), (1, 7, 219), (1, 6, 224), (1, 6, 229), (3, 6, 234), (3, 6, 235), (3, 6, 236), (3, 6, 237), (3, 5, 242), (3, 5, 247), (1, 5, 252), (1, 5, 253), (1, 5, 254), (1, 5, 255), (1, 4, 260), (1, 4, 265), (3, 4, 270), (3, 4, 271), (3, 4, 272), (3, 4, 273), (3, 3, 278), (3, 3, 283), (1, 3, 288), (1, 3, 289), (1, 3, 290), (1, 3, 291), (1, 2, 296), (1, 2, 301), (3, 2, 306), (3, 2, 307), (3, 2, 308), (3, 2, 309), (3, 1, 314), (3, 1, 319), (1, 1, 324), (1, 1, 325), (1, 1, 326), (1, 1, 327), (1, 0, 332), (1, 0, 337)]
import pygame


L=3
# Define the size of the grid
grid_size = 20

# Initialize pygame
pygame.init()

# Create a screen with a size of 400x400 pixels
screen = pygame.display.set_mode((400, 400))
# Define the size of the dot
dot_size = 4

# Define the color of the dot
dot_color = (0, 0, 255)
def draw(i,j,t=0):
    screen.fill((0, 0, 0))
    # Define the color of the points
    point_color = (255, 0, 0)
    for q in range(grid_size):
        v=q * (400 / grid_size)
        if int(t)//L%2==0:
            pygame.draw.line(screen, (50, 50, 50), (0, v), (400, v), 5)
        else:
            pygame.draw.line(screen, (50,50,50), (v,0), (v,400), 5)


    # Loop through the rows and columns of the grid
    for x in range(grid_size):
      for y in range(grid_size):
        # Calculate the coordinates of the point
        point_x = x * (400 / grid_size)
        point_y = y * (400 / grid_size)

        # Draw the point on the screen
        pygame.draw.circle(screen, point_color, (point_x, point_y), 2)
    # Calculate the coordinates of the dot
    dot_x = i * (400 / grid_size)
    dot_y = j * (400 / grid_size)

    # Draw the dot on the screen
    pygame.draw.circle(screen, dot_color, (dot_x, dot_y), dot_size)

    # Update the screen to show the points
    pygame.display.flip()


x,y,t=points.pop(0)
oldx,oldy,oldt=x,y,t
T=0
dT=.01
while points:
    x,y,t=points.pop(0)
    while T<t:
        p=(T-oldt)/(t-oldt)
        i=x*p+oldx*(1-p)
        j=y*p+oldy*(1-p)
        draw(i,j,T)
        T+=dT
    oldx,oldy,oldt=x,y,t
    pygame.time.wait(100)
