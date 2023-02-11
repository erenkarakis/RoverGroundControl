class Data_Model():

    def __int__(self):
        self.temperature = ""
        self.speed = ""
        self.lidar_state = ""
        self.active_cams = ""
        self.velocity = ""

    def __str__(self):
        return f"temp: {self.temperature} speed: {self.speed} lidar_state: {self.lidar_state} " \
               f"active_cams: {self.active_cams} velocity: {self.velocity}"

    def save(self):
        pass
