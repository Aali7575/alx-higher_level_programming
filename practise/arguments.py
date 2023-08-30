#!/usr/bin/python3

import sys
import os
import stat

def main():
    #Check if arguments are provided
    if len(sys.argv) < 3:
        print("Error: 2 arguments required")
        sys.exit(1)

        # Get command line arguments
        args = sys.argv
        command = args[0]
        filename = args[1]


        # Check if file exists
        if not os.path.isfile(filename):
            print(f"File {filename} does not exist")
            sys.exit(1)

            #check if file can be read
            try:
                with open(filename) as f:
                    readable = True
            except PermissionError:
                readable = False

                if not readable:
                    print(f"{filename} is not readable")
                    sys.exit(1)

                else:
                    print(f"{filename} is readable")

                    # Call the main function
                    if __name__ == "__main__":
                        main()

