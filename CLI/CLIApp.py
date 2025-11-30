import cmd

class MyCLI (cmd.cmd):
    # CLI commands and functionality is here
    prompt = '>> ' # Changin the prompt text
    intro = 'Welcome to MyCLI. Type "help" for avialable commands' # Intro message

    def please_Hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def please_quit(self, line):
        """Exit the CLI."""
        return True
    
    
if __name__ == '__main__':
        MyCLI().cmdloop()