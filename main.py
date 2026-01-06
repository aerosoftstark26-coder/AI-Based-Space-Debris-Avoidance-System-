from tle_loader import load_satellite
from sensor_module import SensorModule
from ai_decision import ai_decision
from maneuver import maneuver_strategy
from gui import launch_gui

# Automatically fetch TLE from CelesTrak
sat = load_satellite("ISS")
if sat is None:
    print("Satellite not found in TLE source")