"""
Module for managing platforms.
"""
import pygame

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

FLOOR_1                = (69, 274, 261, 313, 300, 100)
#GRASS_RIGHT           = (576, 576, 70, 70)
#GRASS_MIDDLE          = (504, 576, 70, 70)
#STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
#STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
#STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        #sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        sprite_sheet = SpriteSheet( \
                "images/green-hill-zone/level-fragments/27190.png")

        self.x0 = sprite_sheet_data[0];
        self.y0 = sprite_sheet_data[1];
        self.x1 = sprite_sheet_data[2];
        self.y1 = sprite_sheet_data[3];

        self.image = sprite_sheet.get_image(self.x0, \
                self.y0, self.x1-self.x0, self.y1-self.y0)

        if (len(sprite_sheet_data) > 4):
            a = sprite_sheet_data[4]
            b = sprite_sheet_data[5]
            self.image = pygame.transform.scale(self.image, (a,b))
        
        colorkey = self.image.get_at((0,0))
        self.image.set_colorkey(colorkey)

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """


        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
