import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()


def test(surface):
    pygame.draw.rect(surface, pygame.Color("red"), pygame.Rect((0, 0), (20, 20)))
    return surface


while True:
    s = pygame.Surface((200, 200), pygame.HWSURFACE)
    s.fill((255, 255, 255, 255))

    s = test(s)
    screen.blit(s, (100, 100))

    pygame.display.flip()  # update canvas on screen

    clock.tick(30)
