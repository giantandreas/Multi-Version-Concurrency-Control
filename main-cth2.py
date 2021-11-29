from schedule import Schedule
from storage import *
from mvccTransaction import *

# INISISASI SCHEDULE, STORAGE DAN TRANSACTION
################################################################

# INISIASI STORAGE
storeW = Storage("W", 10, 0, 0)
storeX = Storage("X", 10, 0, 0)
storeY = Storage("Y", 10, 0, 0)
storeZ = Storage("Z", 10, 0, 0)

# INISIASI TRANCSACTION
transaction1 = Transaction(name="T1", ts=1)
transaction2 = Transaction(name="T2", ts=2)
transaction3 = Transaction(name="T3", ts=3)
transaction4 = Transaction(name="T4", ts=4)
transaction5 = Transaction(name="T5", ts=5)


# INISIASI TASK DAN SCHEDULE
# S = R5(X);R2(Y);R1(Y);W3(Y);W3(Z);R5(Z);R2(Z);R1(X);R4(W),W3(W);W5(Y);W5(Z)

task1 = Task(TaskType.READ, storeX, transaction5)
task2 = Task(TaskType.READ, storeY, transaction2)
task3 = Task(TaskType.READ, storeY, transaction1)
task4 = Task(TaskType.WRITE, storeY, transaction3)
task5 = Task(TaskType.WRITE, storeZ, transaction3)
task6 = Task(TaskType.READ, storeZ, transaction5)
task7 = Task(TaskType.READ, storeZ, transaction2)
task8 = Task(TaskType.READ, storeX, transaction1)
task9 = Task(TaskType.READ, storeW, transaction4)
task10 = Task(TaskType.WRITE, storeW, transaction3)
task11 = Task(TaskType.WRITE, storeY, transaction5)
task12 = Task(TaskType.WRITE, storeZ, transaction5)


listOfTasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11]
schedule = Schedule(listOfTasks)

if __name__ == "__main__":
    
    print("Schedule = R5(X);R2(Y);R1(Y);W3(Y);W3(Z);R5(Z);R2(Z);R1(X);R4(W),W3(W);W5(Y);W5(Z)")
    print()
    schedule.execute_schedule()
    print("\n")
    print("###################")
    storeX.print_storage()
    print()
    print("###################")
    storeY.print_storage()

