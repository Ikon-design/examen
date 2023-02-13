#create a class called pump1 with the following attributes
#pump1 has a name, a flow rate, a pressure, and a temperature
class pump:
    def __init__(self, period, execution_time, production):
        self.period = period
        self.execution_time = execution_time
        self.production = production

class machine:
    def __init__(self, period, execution_time, oilNeeded, production):
        self.period = period
        self.execution_time = execution_time
        self.oilNeeded = oilNeeded
        self.production = production

class tank:
    def __init__(self, quantity):
        self.quantity = quantity


p10 = pump(5, 2, 10)
p20 = pump(15, 3, 20)
motorMachine = machine(5, 5, 25, 1)
wheelMachine = machine(5, 3, 5, 1)
t = tank(0)
wheels = 0
motors = 0
execution_time = 0
stockWhells = 0
stockMotors = 0

def production(wheels, motors, execution_time):
  print("Wheels: ", wheels)
  print("Motors: ", motors)
  print("Oil: ", t.quantity)
  
  if motors == 0 and t.quantity > motorMachine.oilNeeded:
    t.quantity -= motorMachine.oilNeeded
    motors += motorMachine.production
    print("Motors are being produced")
    return "motor"
  elif wheels < 4 and t.quantity >= wheelMachine.oilNeeded:
    t.quantity -= wheelMachine.oilNeeded
    wheels += wheelMachine.production
    print("Wheels are being produced")
    return "wheel"
  elif wheels == 4 and motors == 1:
    print("Car is being produced")
    return "car"
  else:
    oil(execution_time)

def oil():
  if t.quantity > 30:
    t.quantity += p10.production
    print("Add 10 liters of oil")
  if t.quantity < 30:
    t.quantity += p20.production
    print("Add 20 liters of oil")
  
def wait(period, execution_time):
  print("Waiting for ", period, " seconds")
  while execution_time < period:
    execution_time += 1
    print("Execution time: ", execution_time)
    oil(execution_time)

while execution_time < 15:
  execution_time += 1
  print("Execution time: ", execution_time)
  value = production(wheels, motors, execution_time)
  if value == "motor":
    motors += motorMachine.production;
  if value == "wheel":
    wheels += wheelMachine.production;
  if value == "car":
    wheels = 0
    motors = 0
    stockWhells += 4
    stockMotors += 1
