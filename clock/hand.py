import math
class Hand():
    def __init__ (self, obj, sprite_name, x_scale, y_scale, dist, initial, step, start_x, start_y):
        self.obj = obj
        self.obj.sprite = sprite(sprite_name)
        self.obj.scaleX = x_scale
        self.obj.scaleY = y_scale
        self.obj.dist = dist
        self.obj.timer = 0
        self.obj.step_value = step
        self.obj.angle =90 - (initial * 6)
        self.start_x = start_x
        self.start_y = start_y
        print(initial, self.obj.angle)
        self.update_pos()
        
        # 0 * 6 -> 90
        # 15 * 6 -> 0
        # 30 * 6 -> -90
        # 45 * 6 -> -180
    
    def update_pos(self):
        self.obj.angleX = math.cos(math.radians(self.obj.angle))
        self.obj.angleY = math.sin(math.radians(self.obj.angle))
        self.obj.x = self.start_x + (self.obj.dist * self.obj.angleX)
        self.obj.y = self.start_y + (self.obj.dist * self.obj.angleY)
        self.obj.angle = self.obj.angle
    
    def tick(self):
        self.obj.timer += 1
        if (self.obj.timer >= 60):
            self.obj.timer = 0
            self.obj.angle -= self.obj.step_value
            self.update_pos()

    
