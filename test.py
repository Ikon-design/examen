import time
import datetime

# Initialisation des variables
wheels = 0
motors = 0
tank = 50
oil_pump1 = 0
oil_pump2 = 0

# Definition des tâches
def pump1():
    global oil_pump1
    oil_pump1 += 10
    print("Pump 1 produced 10 oil")
    time.sleep(2)

def pump2():
    global oil_pump2
    oil_pump2 += 20
    print("Pump 2 produced 20 oil")
    time.sleep(3)

def machine1():
    global wheels, oil_pump1
    if oil_pump1 >= 25:
        oil_pump1 -= 25
        wheels += 1
        print("Machine 1 produced 1 wheel")
        time.sleep(5)

def machine2():
    global motors, oil_pump2
    if oil_pump2 >= 5:
        oil_pump2 -= 5
        motors += 1
        print("Machine 2 produced 1 motor")
        time.sleep(3)

# Definition du planificateur
def scheduler():
    global wheels, motors, tank, oil_pump1, oil_pump2
    current_time = datetime.datetime.now().minute

    if current_time <= 2: # On execute les tâches pendant 2 minutes
        if tank == 50: # Si le réservoir est plein, les pompes ont une priorité faible
            if motors <= wheels / 4: # Si le nombre de moteurs est inférieur au nombre de roues divisé par 4, la machine 1 a une priorité élevée
                machine1()
            else: # Sinon, la machine 2 a une priorité élevée
                machine2()
        else: # Si le réservoir n'est pas plein, les pompes ont une priorité élevée
            if oil_pump1 <= oil_pump2:
                pump1()
            else:
                pump2()
    else:
        print("Time's up")

# Boucle principale
while True:
    scheduler()