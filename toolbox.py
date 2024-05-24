#!/usr/bin/env python3
import cmd
import shlex

class Shell(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(Air): '

    def do_greet(self, fullName):
        names = shlex.split(fullName)
        for name in names:
            print(f"hello {name}")

    def do_sum(self, line):
        nums = [int(num) for num in line.split()]  # Convert input numbers to integers
        total = sum(nums)
        print("Sum:", total)
#        return total  # Return the sum

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys

    if not sys.stdin.isatty():
        print(sys.stdin)
        for command in sys.stdin:
            print(command)
            Shell().onecmd(command)
    else:
        Shell().cmdloop()