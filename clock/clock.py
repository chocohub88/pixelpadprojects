# Function

import math 
from datetime import datetime

class Clock():
    def __init__(self, start_x, start_y, radius, hour, minute, second):
        self.calculated_hour = hour
        self.calculated_minute = minute
        self.calculated_second = second
        self.radius = radius
        self.scale_factor = radius / 150.0
        
        self.second_hand = Hand(HandObj(), "hand.png", 2.8 * self.scale_factor, 0.4 * self.scale_factor, radius/2, self.calculated_second, 6, start_x, start_y)
        self.minute_hand = Hand(HandObj(), "hand.png", 2.5 * self.scale_factor, 0.6 * self.scale_factor, radius/2, self.calculated_minute, 0.1, start_x, start_y)

        hour_initial_value = (self.calculated_hour % 12) * 5 + (self.calculated_minute / 12.0)
        self.hour_hand = Hand(HandObj(), "hand.png", 2.2 * self.scale_factor, 1 * self.scale_factor, radius/2, hour_initial_value, 0.00167, start_x, start_y)
        
        # Align starting position
        self.second_hand.x, self.second_hand.y = start_x, start_y
        self.minute_hand.x, self.minute_hand.y = start_x, start_y
        self.hour_hand.x, self.hour_hand.y = start_x, start_y

        for i in range(60):
            angle = i * 6
            isHour = (i % 5 == 0)
            t = Tick()
            if isHour:
                t.scaleY = 0.8
                t.scaleX = 0.4
                dist = radius - get_width(t) + 108
            else:
                t.scaleX = 0.25
                t.scaleY = 0.4
                dist = radius - get_width(t) + 100
            
            t.x = start_x + (dist * math.cos(math.radians(angle)))
            t.y = start_y + (dist * math.sin(math.radians(angle)))
            t.angle = angle

    @staticmethod
    def convert_from_timezone(base_time, offset_hours):
        new_hour = (base_time.hour + offset_hours) % 24
        return new_hour, base_time.minute, base_time.second

    def update(self):
        self.second_hand.tick()
        self.minute_hand.tick()
        self.hour_hand.tick()
