from bullet import Bullet


class MachineGun(Bullet):
    def __init__(self, damage, velocity, position, overheat_time, visible=True, fire_sound_filename=None, hit_sound_filename=None):
        super().__init__(damage, velocity, position, True, visible, fire_sound_filename, hit_sound_filename)
        self.overheat_time = overheat_time
        self.overheated = False

    def draw(self):
        if self.visible and self.active:
            # NOTE: Normally we wouldn't put a print in here, but this is a substitute for the real draw function
            #  we might use if we were using pygame or pygamezero
            if self.overheated:
                print('Machine Gun', self.position, self.velocity, "I've given her all she's got capt'n")
            else:
                print('Machine Gun', self.position, self.velocity)

    def update(self):
        self.overheated = not self.overheated
        super().update()
