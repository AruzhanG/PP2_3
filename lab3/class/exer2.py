class String:
    def _init_(self):
        self.string = ""
    def get_string(self):
        self.string_input = input()
    def printString(self):
        print(self.string_input.upper())
        
result = String()
result.get_string()
result.printString()

        