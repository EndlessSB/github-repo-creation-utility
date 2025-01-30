class ArgumentHandler:
    def __init__(self):
        self.args = []  # Initialise an empty list to store arguments

    def add_arg(self, arg):
        """Adds a new argument to the args list"""
        self.args.append(arg)
        print(f"Added: {arg}")

    def show_args(self):
        """Displays the current arguments"""
        print("Current arguments:", self.args)
    
    def return_args(self):
        return self.args