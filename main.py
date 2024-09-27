import pygame

pygame.init()

HEIGHT = 800
WIDTH = 1200

main_display = pygame.display.set_mode((HEIGHT, WIDTH))

count = 0
while True:
    print("Hello world!")
    count += 1
    if count >= 10:
        break