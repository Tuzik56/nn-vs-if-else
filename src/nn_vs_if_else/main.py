import os
import sys
import traci

def run():
    step = 0

    while step < 200:
        traci.simulationStep()

        vehicles = traci.vehicle.getIDList()

        for veh_id in vehicles:
            speed = traci.vehicle.getSpeed(veh_id)
            position = traci.vehicle.getPosition(veh_id)

            print(f"Step {step} | ID: {veh_id} | Speed: {speed:.2f} | Position: {position}")

        step += 1

    traci.close()


if __name__ == "__main__":

    if "SUMO_HOME" not in os.environ:
        sys.exit("Declare environment variable 'SUMO_HOME'")

    sumo_binary = "sumo-gui"
    sumo_config = "sumo_project/test.sumocfg"

    traci.start([sumo_binary, "-c", sumo_config])

    run()