from typing import List
import storage


# Kelas untuk mereperesentasikan Transaction
class Transaction:
    def __init__(self, name:str, ts:int) -> None:
        self.name = name
        self.ts = ts
    
    def get_read_TS(self):
        return self.rTS

    def get_write_TS(self):
        return self.wTS

# Type untuk task, read atau write
class TaskType:
    WRITE = "write"
    READ = "read"


# Task merepresentasikan task yang akan dilakukan
# akan disimpan dalam list schedule
class Task:
    def __init__(self, type:TaskType, Q:storage.Storage, transaction:Transaction):
        self.type = type
        self.target = Q
        self.transaction = transaction

    def get_task_TS(self):
        return self.transaction.ts

    def execute(self):
        timeStampT = self.get_task_TS()
        # JIKA READ
        if(self.type == TaskType.READ):
            # Mencari storage dan versionnya yang memiliki WTS paling besar namun < timestamp Transaksi
            strg = self.target.get_larges_wts_storage(timeStampT)

            # MENGUPDATE rts dari Q jika RTS < TS Transaksi
            if(strg.rTS < timeStampT):
                strg.rTS = timeStampT
            content = strg.read()

            print(f"Read {strg.name} , Content = {content}")

            return
        
        # JIKA WRITE
        elif(self.type == TaskType.WRITE):

            # Mencari storage dan versionnya yang memiliki WTS paling besar namun < timestamp Transaksi
            strg = self.target.get_larges_wts_storage(timeStampT)

            if(timeStampT < strg.rTS or strg == False):
                print("ROLL BACK!!")
                # Implementasi Roll back
                exit()
            elif (strg.wTS == timeStampT):
                rt = strg.write(value=None)
                strg.wTS = timeStampT
                if(rt != False):
                    print(f"Write {strg.name}")
                else:
                    print("Somthign WRONG")
            else:
                # buat version
                print(f"Create Version from {strg.name}")
                version = storage.Version(strg, ts=timeStampT)
                version.rTS = timeStampT
                version.wTS = timeStampT
                version.write(value=None)
            return

        print("This should not apear")
