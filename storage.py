

class Storage:
    # Content berisi int aja keknya
    # misalkan nanti ini nama storagenya A
    # truss ada operasi read A, misalnya gitu
    def __init__(self, name:str, content:int, Wts:int, Rts:int) -> None:
        self.name = name
        self.content = content
        self.wTS = Wts
        self.rTS = Rts
        self.version = []

    def read(self):
        self.print_timestamp()
        return self.content

    def write(self, value:int):
        self.print_timestamp()
        if(value != None):
            self.content = value
        return True

    def get_larges_wts_storage(self, ts:int):
        vers = None
        in_version = False
        for strg in self.version:
            if strg.wTS < ts:
                in_version = True
                vers = strg
        
        if in_version:
            return vers
        else:
            if self.wTS < ts:
                return self
            else:
                return False


    def print_storage(self):
        print(f"Content = {self.content}")
        print(f"Write TS = {self.wTS}")
        print(f"Read TS = {self.rTS}")
        print("version = ", end="")
        for ver in self.version:
            print(ver.name, end="")
            print(",", end="")
        print()

    def print_timestamp(self):
        print(f"TS {self.name} = ({self.rTS},{self.wTS})", end=" ")


class Version(Storage):
    
    def __init__(self, parent:Storage, ts:int) -> None:
        self.name = parent.name + str(ts)
        self.content = parent.content
        self.wTS = parent.wTS
        self.rTS = parent.rTS
        self.version = parent.version

        parent.version.append(self)

