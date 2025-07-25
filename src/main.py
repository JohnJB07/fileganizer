# Libraries
import os

# Modules
import directory, options

class Main:
    def __init__(self):
        self.exit = False
        self.directory = directory.Directory
        self.json_file = self.directory.openJsonFile()
        self.user_input()
    
    def user_input(self):
        options.Print.returnLogo()
        while not self.exit:
            options.Print.printLine()
            
            token = input("Input here: ").lower()
            if token == "exit" or token == "break":
                self.exit = True
            elif token == "get_cwd":
                print("Current directory: ",self.directory.getCurrentDirectory())
            elif token == "create_folders":
                for items in self.json_file["FILES"]["PRESET"]:
                    directory.Directory.makeDirectory(items)
            elif token == "cmds":
                options.Print.printCommands(self.json_file)
            elif token[:3] == "cd ":
                directory.Directory.changeDirectory(token[3:])
            elif token[:8] == "makedir ":
                directory.Directory.makeDirectory(token[8:])
            else:
                print(f"Command '{token}' could not be recognized")
                continue
            
if __name__ == '__main__':
    Main()
