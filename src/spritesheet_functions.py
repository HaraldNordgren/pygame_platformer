"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame

import constants

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height, transparent = False):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
       
        image = None

        if (transparent):
            image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
            image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
            image = image.convert_alpha()
        else:
            image = pygame.Surface([width, height])
            image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
            image = image.convert()
            image.set_colorkey(constants.BLACK)
        
        #if (scale_factor):
        #    image = pygame.transform.scale(image, scale_factor)

        # Return the image
        return image
