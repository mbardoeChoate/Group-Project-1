
class Motor_Controller:
    def __init__(self):
        self.motor = Motor()
        self.encoder = Encoder()


    def set_position(self, position):
        diff=position-self.encoder.get_position()
        speed = min(max(self.kp*diff, -1),1)
        self.motor.set_speed(speed)

    def set_speed(self, speed):
        self.motor.set_speed(speed)

    def update(self):
        self.encoder.update()


class Motor:
    def __init__(self, inverted=False):
        self.inverted = inverted
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed

    def reverse(self):
        self.speed = -self.speed

    def get_speed(self):
        return self.speed

    def stop(self):
        self.speed = 0


class Encoder:
    def __init__(self, num_of_clicks=60):
        self.position = 0
        self.num_of_clicks = num_of_clicks

    def get_position(self):
        return self.position

    def reset(self):
        self.position = 0

    def update(self, turns):
        self.position += turns*self.num_of_clicks
