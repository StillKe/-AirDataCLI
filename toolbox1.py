#!/usr/bin/env python3
import cmd
import shlex

class Shell(cmd.Cmd):
    """Airbnb command processor example."""
    prompt = '(Airbnb): '

    def do_greet(self, fullName):
        names = shlex.split(fullName)
        for name in names:
            print(f"hello {name}")

    def do_sum(self, line):
        nums = [int(num) for num in line.split()]  # Convert input numbers to integers
        total = sum(nums)
        print("Sum:", total)

    def do_deploy(self, service):
        """Deploy a service"""
        print(f"Deploying {service}...")

    def do_fetch_logs(self, service):
        """Fetch logs for a service"""
        print(f"Fetching logs for {service}...")

    def do_backup(self, resource):
        """Backup a resource"""
        print(f"Backing up {resource}...")

    def do_restore(self, resource):
        """Restore a resource"""
        print(f"Restoring {resource}...")

    def do_health_check(self, service):
    """Check health status of a service"""
    print(f"Health check for {service}...")


    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    import sys

    if not sys.stdin.isatty():
        for command in sys.stdin:
            Shell().onecmd(command.strip())
    else:
        Shell().cmdloop()
