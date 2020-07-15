class Bullet:
    def __init__(self, damage, velocity, position, active=False, visible=True, fire_sound_filename=None, hit_sound_filename=None):
        self.damage = damage
        self.velocity = velocity
        self.position = position
        self.active = active
        self.visible = visible
        self.fire_sound_filename = fire_sound_filename
        self.hit_sound_filename = hit_sound_filename

    def update(self):
        self.position = self.position + self.velocity

    def draw(self):
        if self.visible and self.active:
            # NOTE: Normally we wouldn't put a print in here, but this is a substitute for the real draw function
            #  we might use if we were using pygame or pygamezero
            print('Bullet', self.position, self.velocity)

    def destroy(self):
        self.active = False
        self.visible = False

    def apply_damage(self, hit_object):
        print(self.damage, 'damage done to', hit_object)

    def fire(self):
        if not self.active:
            self.active = True

