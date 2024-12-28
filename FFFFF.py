key_switch_camera = "c"
key_switch_mode = "z"
key_forward = "w"
key_back = "s"
key_left = "a"
key_right = "d"
key_up = "space"
key_down = "shift"
key_turn_left = "h"
key_turn_right = "e"
step = 0.2
class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
    def cameraUp(self):
        x, y, z = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-x, -y, -z, -3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() -5) %360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
    def look_at(self, angle):
        x_from = self.hero.getX()
        y_from = self.hero.getY()
        z_from = self.hero.getZ()
        dx, dy = self.check_dir(angle)
        x_to = x_from +dx
        y_to = y_from + dy
        return x_to, y_to, z_from
    def just_move(self, angle):
        x, y, z = self.look_at(angle)
        if not self.land.isBlockAt((round(x), round(y), round(z))):
            self.hero.setPos((x, y, z))
            print(f"Герой переміщенний на {(x, y, z)}")
        else:
            print(f"Неможливо рухатись, є блок на {(x, y, z)}")

