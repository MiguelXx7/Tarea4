import pybullet as p
import pybullet_data
import time
import random

def run_random_sequence(total_moves=8, transition_steps=500, hold_steps=120, sleep=1./240.):
    p.connect(p.GUI)
    p.setGravity(0,0,-9.8)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.resetDebugVisualizerCamera(1.5, 50, -35, [0,0,0.5])

    p.loadURDF("plane.urdf")
    robot = p.loadURDF("two_joint_robot_custom.urdf",[0,0,0.1],useFixedBase=True)

    # Empieza desde 0,0
    prev = (0.0, 0.0)

    for move in range(total_moves):
        # Genera nueva pose aleatoria en rango [-π, π]
        target = (random.uniform(-3.14,3.14), random.uniform(-3.14,3.14))
        print(f"Movimiento {move+1}/{total_moves}: {target}")

        # Interpola de prev a target
        for i in range(transition_steps):
            α = i/transition_steps
            j1 = prev[0]*(1-α) + target[0]*α
            j2 = prev[1]*(1-α) + target[1]*α
            p.setJointMotorControl2(robot, 0, p.POSITION_CONTROL, j1, force=500)
            p.setJointMotorControl2(robot, 1, p.POSITION_CONTROL, j2, force=500)
            p.stepSimulation(); time.sleep(sleep)

        # Mantén la pose un rato
        for _ in range(hold_steps):
            p.stepSimulation(); time.sleep(sleep)

        prev = target

    input("¡Secuencia rara completada! Presiona Enter para salir…")
    p.disconnect()

if __name__=="__main__":
    run_random_sequence(total_moves=10, transition_steps=800, hold_steps=240)

