import numpy as np

class SensorModule:
    def detect(self, sat_pos, debris_pos):
        relative = debris_pos - sat_pos
        distance = np.linalg.norm(relative)
        return distance, relative