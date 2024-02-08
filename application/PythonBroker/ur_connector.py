from urinterface.robot_connection import RobotConnection
import numpy as np
from pathlib import Path
import time
import msvcrt



v0 = 1.0
a0 = 5.0
vm_ip = "192.168.230.128"
ur5e = RobotConnection(vm_ip) # Establish dashboard connection (port 29999) and controller connection (port 30002)

f_name = "test_motion1.csv"
filename = Path("test_results") / Path(f_name)
config_file =  Path("resources") / Path("record_configuration.xml")
ur5e.start_recording(filename=filename, overwrite=True, frequency=50, config_file=config_file, publish_topic=["actual_q"]) # start recording and place the recorded data in test_motion.csv

time.sleep(1)

while True:
    try:

        k = msvcrt.getwche()
        if k == "c":
            break
        elif k in {"1","2"}:
            if k == "1":
                ur5e.movej(np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]), v=1.0, a=0.5)
            if k == "2":
                ur5e.load_program("/program1.urp")
                ur5e.play_program()
        # reset k
        k = "a"
    except KeyboardInterrupt:
        break

ur5e.stop_recording()