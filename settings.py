class Settings:
    """ A class to store all settings for Alien Invasion """

    def __init__(self):
        """ Initialize the games settings """
        # Screen settings
        self.use_fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed = 1.5