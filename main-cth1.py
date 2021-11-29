from schedule import Schedule
from storage import *
from mvccTransaction import *

# INISISASI SCHEDULE, STORAGE DAN TRANSACTION
################################################################

# INISIASI STORAGE
storeX = Storage("X", 10, 0, 0)
storeY = Storage("Y", 10, 0, 0)

# INISIASI TRANCSACTION T1
transaction1 = Transaction(name="T1", ts=1)
taska1 = Task(type=TaskType.READ, Q=storeX, transaction=transaction1)
taska2 = Task(type=TaskType.WRITE, Q=storeY, transaction=transaction1)

# INISIASI TRANSACTION T2
transaction2 = Transaction(name="T2", ts=2)
taskb1 = Task(type=TaskType.WRITE, Q=storeX, transaction=transaction2)
taskb2 = Task(type=TaskType.WRITE, Q=storeY, transaction=transaction2)

# INISIASI TRANSACTION T3
transaction3 = Transaction(name="T3", ts=3)
taskc1 = Task(type=TaskType.WRITE, Q=storeY, transaction=transaction3)

# INISIASI SCHEDULE
# S = R1(X);W2(X);W2(Y);W3(Y);W1(Y);C1;C2;C3

listOfTasks = [taska1, taskb1, taskb2, taskc1, taska2]
schedule = Schedule(listOfTasks)

if __name__ == "__main__":
    print("Schedule = R1(X);W2(X);W2(Y);W3(Y);W1(Y);C1;C2;C3")
    print()
    
    schedule.execute_schedule()
    print("\n")
    print("Schedule completed")
    print("\n")

    print("###################")
    storeX.print_storage()
    print()
    print("###################")
    storeY.print_storage()

