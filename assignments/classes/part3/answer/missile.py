from bullet import Bullet


class Missile(Bullet):
    def __init__(self, damage, velocity, position, target, active=True, visible=True, fire_sound_filename=None, hit_sound_filename=None):
        super().__init__(damage, velocity, position, active, visible, fire_sound_filename, hit_sound_filename)
        self.target = target

    def draw(self):
        if self.visible and self.active:
            # NOTE: Normally we wouldn't put a print in here, but this is a substitute for the real draw function
            #  we might use if we were using pygame or pygamezero
            print('Missile', self.position, self.velocity, 'smoke', self.target)
