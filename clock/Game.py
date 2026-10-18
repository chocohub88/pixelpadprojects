# Game Start

from datetime import datetime
self.now = datetime.utcnow()

h,m,s = Clock.convert_from_timezone(self.now,-7)
self.clock = Clock(-200,50,100, h,m,s) #now
h2,m2,s2 = Clock.convert_from_timezone(self.now,0)
self.clock2 = Clock(300,50,100, h2,m2,s2) #london

# Game Loop
self.clock.update()
self.clock2.update()

