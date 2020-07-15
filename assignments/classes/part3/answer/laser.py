from bullet import Bullet


class Laser(Bullet):
    def __init__(self, damage, velocity, position, visible=True, fire_sound_filename=None, hit_sound_filename=None):
        super().__init__(damage, velocity, position, True, visible, fire_sound_filename, hit_sound_filename)

    def draw(self):
        if self.visible and self.active:
            # NOTE: Normally we wouldn't put a print in here, but this is a substitute for the real draw function
            #  we might use if we were using pygame or pygamezero
            print('Laser', self.position, self.velocity)
