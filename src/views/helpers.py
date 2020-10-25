import pygame

from settings.display import DISPLAY_SCALING


def get_text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def create_message(text, pos, font='freesansbold.ttf', size=60, color=pygame.Color("black"), center=True):
    pos_x, pos_y = pos

    large_text = pygame.font.SysFont(font, size * DISPLAY_SCALING)
    text_surf, text_rect = get_text_objects(text, large_text, color)
    
    if center:
        text_rect.center = (pos_x, pos_y)
    else:
        text_rect.topleft = (pos_x, pos_y)
    
    return text_surf, text_rect


def draw_color_box(surface, border_color, border_thickness, inner_color, coords, size):
    """Coords: (x, y); Size (w, h)"""
    x, y = coords  # todo pass these as named tuples
    w, h = size
    
    pygame.draw.rect(surface, border_color, (x, y, w, h))
    pygame.draw.rect(surface, inner_color,
                     (x+border_thickness, y+border_thickness, w-2*border_thickness, h-2*border_thickness))
